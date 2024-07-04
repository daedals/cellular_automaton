import numpy as np

class Canvas:
    def __init__(self, width=500, height=500):
        self.width = width
        self.height = height

        self.canvas_states : np.ndarray = np.zeros((width, height), dtype=np.uint8)
        self.canvas_change_flags : np.ndarray = np.zeros((width, height), dtype=np.uint8)
        self.canvas_rgb : np.ndarray = np.zeros((width, height, 3), dtype=np.uint8)

    def step(self):
        for (x,y), value in np.ndenumerate(self.canvas_rgb):
            pass

    def draw(self, x, y, color):
        radius = 10
        x, y = x-1, y-1
        for _x in range(max(0, x-radius), min(self.width-1, x+radius)):
            for _y in range(max(0, y-radius), max(self.height-1, y+radius)):
                if (_x - x)**2 + (_y - y)** 2 < radius**2:
                    self.canvas_rgb[_x, _y] = color

    def get_canvas(self):
        return self.canvas_rgb
