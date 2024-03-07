from intersection import Intersection


class Intersections:
    def __init__(self, ROW_NUM, COL_NUM, X, Y):
        """
        X, Y are the coordinates of the top left point
        """
        self.SPACING = 50
        self.ROW_NUM = ROW_NUM
        self.COL_NUM = COL_NUM
        self.X = X
        self.Y = Y
        self.grid = [[Intersection
                      (self.X + j * self.SPACING, self.Y + i * self.SPACING)
                      for j in range(COL_NUM)] for i in range(ROW_NUM)]
        self.count = ROW_NUM * COL_NUM
        self.occupied = [[False for _ in range(COL_NUM)]
                         for _ in range(ROW_NUM)]
        self.stone_colors = [[0 for _ in range(COL_NUM)]
                             for _ in range(ROW_NUM)]

    def display(self):
        for i in self.grid:
            for j in i:
                j.display()

    def add_gridlines(self):
        stroke(0)
        strokeWeight(1)

        for i in range(self.COL_NUM):
            line(self.X + i * self.SPACING, self.Y, self.X + i * self.SPACING,
                 self.Y + self.SPACING * (self.ROW_NUM - 1))

        for j in range(self.ROW_NUM):
            line(self.X, self.Y + j * self.SPACING,
                 self.X + self.SPACING * (self.COL_NUM - 1),
                 self.Y + j * self.SPACING)

    def mark_occupied(self, intersection, color, occupied=True):
        for i, row in enumerate(self.grid):
            for j, inter in enumerate(row):
                if inter == intersection:
                    self.occupied[i][j] = occupied
                    if color == 'black':
                        self.stone_colors[i][j] = 1
                    else:
                        self.stone_colors[i][j] = 2
                    return

    def is_occupied(self, intersection):
        for i, row in enumerate(self.grid):
            for j, inter in enumerate(row):
                if inter == intersection:
                    return self.occupied[i][j]
        return False

    def is_full(self):
        for row in self.occupied:
            if not all(row):
                return False
        return True
