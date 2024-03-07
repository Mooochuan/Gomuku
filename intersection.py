class Intersection:
    """An intersection point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        """Draws the point"""
        fill(0)
        ellipse(self.x, self.y, 5, 5)
