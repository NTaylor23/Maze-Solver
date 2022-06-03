import cv2

def note_exit(line, row):
    i, j = 0, len(line) - 1
    while line[i] != 'o':
        i += 1
    while line[j] != 'o':
        j -= 1
    return row, (i + j) // 2

class ProcessImage:
    def __init__(self, img):
        self.img = cv2.imread(img, 1)
        self.matrix = self.conv_matrix()
        self.start = note_exit(self.matrix[0], 0)
        self.end = note_exit(self.matrix[-1], len(self.matrix) - 1)

    def conv_matrix(self):
        result, line_builder = [], []
        for line in self.img:
            for group in line:
                if group[0] == 255:
                    line_builder.append('o')
                else:
                    line_builder.append('x')
            result.append(line_builder)
            line_builder = []
        return result
