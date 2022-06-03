import cv2
import numpy as np

class WriteImage:
    def __init__(self, solved_maze):
        self.solved_maze = solved_maze
        self.as_np = self.to_np_array()
        self.img = self.create_image()

    def to_np_array(self):
        result = []
        for line in self.solved_maze:
            new_line = []
            for element in line:
                if element == '.':
                    new_line.append([0, 100, 0])
                elif element == 'o':
                    new_line.append([255, 255, 255])
                else:
                    new_line.append([0, 0, 0])
            result.append(new_line)

        as_np = np.array(result)
        return as_np

    def create_image(self):
        return cv2.imwrite('assets/maze.png', self.as_np)

