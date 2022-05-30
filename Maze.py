"""
s x o x o o o o
o x o o o x x o
o o x o x o o o
x o o o x o x o
o x o x o o x o
o o o x o x o o
o x x x o x o x
o o x o o x o e

Positional Constraints:
x, y cannot be <0 or >7

"""


def create_matrix(m_string):
    # Works
    res = []
    for line in m_string:
        res.append(list(line))
    return res


class Maze:
    def __init__(self, maze_string):
        self.maze_string = maze_string
        self.as_lines = self.maze_string.split('\n')
        self.matrix = create_matrix(self.as_lines)
        self.walls = set(self.find_walls())

    def find_width_height(self):
        return [len(self.as_lines[0]), len(self.as_lines)]

    def find_start_end(self):
        start, end = tuple(), tuple()
        i = 0
        for line in self.matrix:
            if line.__contains__('s'):
                start = (i, line.index('s'))
            elif line.__contains__('e'):
                end = (i, line.index('e'))
            i += 1
        return start, end

    def find_walls(self):
        res = []
        for i in range(len(self.as_lines)):
            for j in range(len(self.as_lines[i])):
                if self.as_lines[i][j] == 'x':
                    res.append((i, j))
        return res

    def solve_maze(self):
        start, end = self.find_start_end()
        i, j = start
        visited = set()




str = """sxoxoooo
oxoooxxo
ooxoxooo
xoooxoxo
oxoxooxo
oooxoxoo
oxxxoxox
ooxooxoe"""

test_maze = Maze(str)
print(test_maze.find_walls())
