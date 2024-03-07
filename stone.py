class Stone:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color

    def display(self):
        stroke(0)
        strokeWeight(2)

        if self.color == "black":
            fill(0)
        else:
            fill(255)
        circle(self.x, self.y, 40)
