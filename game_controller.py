
class GameController:
    """
    Win check, announce win and name prompt
    """
    def __init__(self, ROW_NUM, COL_NUM, intersections):
        self.white_wins = False
        self.black_wins = False
        self.ROW_NUM = ROW_NUM
        self.COL_NUM = COL_NUM
        self.intersections = intersections

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def check_horizontal_win(self, color):
        for i in range(self.ROW_NUM):
            count = 0
            for j in range(self.COL_NUM):
                if self.intersections.stone_colors[i][j] == color:
                    count += 1
                    if count >= 5:
                        return True
                else:
                    count = 0
        return False

    def check_vertical_win(self, color):
        for j in range(self.COL_NUM):
            count = 0
            for i in range(self.ROW_NUM):
                if self.intersections.stone_colors[i][j] == color:
                    count += 1
                    if count >= 5:
                        return True
                else:
                    count = 0
        return False

    def check_diagonal_win(self, color):
        for i in range(self.ROW_NUM - 4):
            for j in range(self.COL_NUM - 4):
                count = 0
                for k in range(5):
                    if self.intersections.stone_colors[i + k][j + k] == color:
                        count += 1
                        if count >= 5:
                            return True
                    else:
                        count = 0
        return False

    def check_reverse_diagonal_win(self, color):
        for i in range(4, self.ROW_NUM):
            for j in range(self.COL_NUM - 4):
                count = 0
                for k in range(5):
                    if self.intersections.stone_colors[i - k][j + k] == color:
                        count += 1
                        if count >= 5:
                            return True
                    else:
                        count = 0
        return False

    def check_win(self, color):
        return (self.check_horizontal_win(color) or
                self.check_vertical_win(color) or
                self.check_diagonal_win(color) or
                self.check_reverse_diagonal_win(color))

    def update(self, color):
        """Carries out necessary actions if computer or player wins"""
        if color == "black":
            fill(1)
            textSize(50)
            text("Black wins!", 425, 500)
            self.black_wins = True
        if color == "white":
            fill(1)
            textSize(50)
            text("White wins!", 425, 500)
            self.white_wins = True
