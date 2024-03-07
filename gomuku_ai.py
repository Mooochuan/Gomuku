class ChessAI():
    def __init__(self, chess_len):
        self.len = chess_len
        CHESS_TYPE_NUM = 8
        # [horizon, vertical, left diagonal, right diagonal]
        self.count = [[0 for x in range(CHESS_TYPE_NUM)] for i in range(2)]
        self.pos_score = [[(7 - max(abs(x - 7), abs(y - 7)))
                           for x in range(chess_len)]
                          for y in range(chess_len)]

    def reset(self):
        for i in range(len(self.count)):
            for j in range(len(self.count[0])):
                self.count[i][j] = 0

        self.save_count = 0

    # get all positions that is empty
    def genmove(self, board):
        moves = []
        for y in range(self.len):
            for x in range(self.len):
                if board[y][x] == 0:
                    score = self.pos_score[y][x]
                    moves.append((score, x, y))

        moves.sort(reverse=True)
        return moves

    def search(self, board):
        moves = self.genmove(board)
        bestmove = None
        max_score = -0x7fffffff
        for score, x, y in moves:
            board[y][x] = 2
            score = self.evaluate(board)
            board[y][x] = 0

            if score > max_score:
                max_score = score
                bestmove = (max_score, x, y)
        return bestmove

    def findBestChess(self, board):
        score, x, y = self.search(board)
        return (x, y)

    def getScore(self, mine_count, opponent_count):
        FIVE = 7
        FOUR, THREE, TWO = 6, 4, 2
        SFOUR, STHREE, STWO = 5, 3, 1
        mscore, oscore = 0, 0
        if mine_count[FIVE] > 0:
            return (10000, 0)
        if opponent_count[FIVE] > 0:
            return (0, 10000)

        if mine_count[SFOUR] >= 2:
            mine_count[FOUR] += 1

        if opponent_count[FOUR] > 0:
            return (0, 9050)
        if opponent_count[SFOUR] > 0:
            return (0, 9040)

        if mine_count[FOUR] > 0:
            return (9030, 0)
        if mine_count[SFOUR] > 0 and mine_count[THREE] > 0:
            return (9020, 0)

        if opponent_count[THREE] > 0 and mine_count[SFOUR] == 0:
            return (0, 9010)

        if (mine_count[THREE] > 1 and opponent_count[THREE]
                == 0 and opponent_count[STHREE] == 0):
            return (9000, 0)

        if mine_count[SFOUR] > 0:
            mscore += 2000

        if mine_count[THREE] > 1:
            mscore += 500
        elif mine_count[THREE] > 0:
            mscore += 100

        if opponent_count[THREE] > 1:
            oscore += 2000
        elif opponent_count[THREE] > 0:
            oscore += 400

        if mine_count[STHREE] > 0:
            mscore += mine_count[STHREE] * 10
        if opponent_count[STHREE] > 0:
            oscore += opponent_count[STHREE] * 10

        if mine_count[TWO] > 0:
            mscore += mine_count[TWO] * 4
        if opponent_count[TWO] > 0:
            oscore += opponent_count[TWO] * 4

        if mine_count[STWO] > 0:
            mscore += mine_count[STWO] * 4
        if opponent_count[STWO] > 0:
            oscore += opponent_count[STWO] * 4

        return (mscore, oscore)

    def evaluate(self, board):
        FOUR, THREE, TWO = 6, 4, 2
        SFOUR, STHREE, STWO = 5, 3, 1
        self.reset()
        mine_count = self.count[0]
        opponent_count = self.count[1]
        for i in range(15):
            for j in range(15):
                if board[i][j] == 1 or board[i][j] == 2:
                    current_color = board[i][j]
                    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
                    for d in directions:
                        dx, dy = d
                        count = 1
                        empty = 0
                        temp_i, temp_j = i, j
                        while True:
                            temp_i += dx
                            temp_j += dy
                            if (temp_i < 0
                                    or temp_i >= 15
                                    or temp_j < 0 or temp_j >= 15):
                                break
                            if board[temp_i][temp_j] == 0:
                                empty += 1
                                break
                            elif board[temp_i][temp_j] == current_color:
                                count += 1
                            else:
                                break
                        if count == 4 and empty == 1:
                            if current_color == 1:
                                opponent_count[SFOUR] += 1
                            else:
                                mine_count[SFOUR] += 1
                        elif count == 4 and empty == 0:
                            if current_color == 1:
                                opponent_count[FOUR] += 1
                            else:
                                mine_count[FOUR] += 1
                        elif count == 3 and empty == 1:
                            if current_color == 1:
                                opponent_count[STHREE] += 1
                            else:
                                mine_count[STHREE] += 1
                        elif count == 3 and empty == 0:
                            if current_color == 1:
                                opponent_count[THREE] += 1
                            else:
                                mine_count[THREE] += 1
                        elif count == 2 and empty == 1:
                            if current_color == 1:
                                opponent_count[STWO] += 1
                            else:
                                mine_count[STWO] += 1
                        elif count == 2 and empty == 0:
                            if current_color == 1:
                                opponent_count[TWO] += 1
                            else:
                                mine_count[TWO] += 1
        mscore, oscore = self.getScore(mine_count, opponent_count)
        return (mscore - oscore)
