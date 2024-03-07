from intersections import Intersections
from stone import Stone
from stack import Stack
from game_controller import GameController
from score_recorder import ScoreRecorder
from gomuku_ai import ChessAI
import time
to_draw = Stack()

WIDTH = 850
HEIGHT = 850
ROW_NUM = 15
COL_NUM = 15
X = 75
Y = 75
MAX_DISTANCE = 37.5

intersections = Intersections(ROW_NUM, COL_NUM, X, Y)
gc = GameController(ROW_NUM, COL_NUM, intersections)
sr = ScoreRecorder()
ai = ChessAI(ROW_NUM)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB)


def draw():
    background(153, 126, 76)
    intersections.display()
    intersections.add_gridlines()
    for stone in to_draw.get_items():
        stone.display()
    if intersections.is_full():
        textAlign(CENTER, CENTER)
        textSize(32)
        fill(255, 0, 0)
        text("Game Over", width / 2, height / 2)
        time.sleep(2)
        name = input('Please enter your name')
        if gc.black_wins is True:
            sr.record(name, "win")
            sr.write_sorted_scores_to_file()
        if gc.white_wins is True:
            sr.record(name, "lose")
            sr.write_sorted_scores_to_file()
        exit()
    if gc.check_win(1):
        gc.update("black")
        intersections.occupied = [[True for _ in range(COL_NUM)]
                                  for _ in range(ROW_NUM)]
    if gc.check_win(2):
        gc.update("white")
        intersections.occupied = [[True for _ in range(COL_NUM)]
                                  for _ in range(ROW_NUM)]


def mousePressed():
    if not intersections.is_full():
        # Human player's move
        nearestIntersection = getNearestIntersection(mouseX,
                                                     mouseY,
                                                     intersections)
        if (nearestIntersection is not None
                and not intersections.is_occupied(nearestIntersection)):
            color = "black"
            to_draw.push(Stone(nearestIntersection.x,
                               nearestIntersection.y,
                               color))
            intersections.mark_occupied(nearestIntersection, color)
        computer_move()


def getNearestIntersection(x, y, intersections):
    nearestIntersection = None
    minDistance = float('inf')

    for row in intersections.grid:
        for intersection in row:
            if not intersections.is_occupied(intersection):
                distance = dist(x, y, intersection.x, intersection.y)
                if distance < minDistance and distance <= MAX_DISTANCE:
                    minDistance = distance
                    nearestIntersection = intersection

    return nearestIntersection


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def computer_move():
    if not intersections.is_full():
        board = intersections.stone_colors
        corr = ai.findBestChess(board)
        x = corr[0]
        y = corr[1]
        intersection = intersections.grid[y][x]
        if not intersections.is_occupied(intersection):
            color = "white"
            to_draw.push(Stone(intersection.x, intersection.y, color))
            intersections.mark_occupied(intersection, color)
