import cv2

def note_exit(line: list, row: int) -> tuple:
    """ find the entry/exit point of the maze inside the first row

    Args:
        line (list): the row, being either the first (for start) or last (for end)
        row (int): the row's index

    Returns:
        tuple: point with x and y value
    """
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

    def conv_matrix(self) -> list:
        """ read each pixel of the starting image, and create a list of 'o' characters
        for empty space (white), and 'x' characters for obstacles (black)

        Returns:
            list: a list representation of the original image
        """
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
