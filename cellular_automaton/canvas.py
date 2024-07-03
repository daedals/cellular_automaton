import numpy as np

class Canvas:
    def __init__(self, width=500, height=500):
        self.width = width
        self.height = height
        self.canvas : np.ndarray = np.zeros((height, width, 3), dtype=np.uint8)

    def step(self):
        for (x,y), value in np.ndenumerate(self.canvas):
            pass

    def draw(self, x, y, color):
        self.canvas[y, x] = color

    def get_canvas(self):
        return self.canvas
