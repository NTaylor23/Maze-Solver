import cv2
import numpy as np

class WriteImage:

    def __init__(self, solved_maze, heatmap, max_value):
        self.solved_maze = solved_maze
        self.hm = heatmap
        self.max_value = max_value
        self.as_np = self.to_np_array()

    def to_np_array_indexed(self):
        result = []
        for i in range(len(self.solved_maze)):
            new_line = []
            for j in range(len(self.solved_maze[i])):
                if self.solved_maze[i][j] != 'x':
                    distance = self.hm[i][j]
                    r = int((distance / self.max_value) * 255)
                    new_line.append([255 - r, r, 255])
                else:
                    new_line.append([0, 0, 0])
            result.append(new_line)
        as_np = np.array(result)
        return as_np

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

    def create_image(self, output_path):
        return cv2.imwrite(output_path, self.as_np)

