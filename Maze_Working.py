"""
s  x  o  x  o  o  o  o
o  x  o  o  o  x  x  o
o  o  x  o  x  o  o  o
x  o  o  o  x  o  x  o
o  x  o  x  o  o  x  o
o  o  o  x  o  x  o  o
o  x  x  x  o  x  o  x
o  o  x  o  o  x  o  e
"""


def create_matrix(m_string):
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
        self.width, self.height = self.find_width_height()

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

    def out_of_bounds(self, ver, hor, visited):
        if ver not in range(0, self.height) or hor not in range(0, self.width):
            return True
        elif (ver, hor) in visited:
            return True
        elif self.matrix[ver][hor] == 'x':
            return True
        return False

    def solve_maze(self):
        start, end = self.find_start_end()
        i, j = end
        visited = set()
        distances = list(self.matrix.copy())

        def flood_fill(ver, hor, grid, dist):
            if self.out_of_bounds(ver, hor, visited):
                return
            if self.matrix[ver][hor] == 's':
                grid[ver][hor] = dist
                return grid
            visited.add((ver, hor))
            grid[ver][hor] = dist
            dist += 1
            flood_fill(ver, hor - 1, grid, dist)  # Go left
            flood_fill(ver, hor + 1, grid, dist)  # Go right
            flood_fill(ver - 1, hor, grid, dist)  # Go up
            flood_fill(ver + 1, hor, grid, dist)  # Go down

        flood_fill(i, j, distances, 0)
        self.matrix = create_matrix(self.as_lines)  # Why does the original matrix get effected by flood_fill?
        i, j = start
        visited.clear()

        def generate_path(ver, hor, distance):
            if self.out_of_bounds(ver, hor, visited):
                return
            if distances[ver][hor] > distance:
                return
            if distances[ver][hor] == 0:
                self.matrix[ver][hor] = '√'
                return self.matrix
            visited.add((ver, hor))
            self.matrix[ver][hor] = '.'
            loc = distances[ver][hor]
            generate_path(ver, hor - 1, loc)  # Go left
            generate_path(ver, hor + 1, loc)  # Go right
            generate_path(ver - 1, hor, loc)  # Go up
            generate_path(ver + 1, hor, loc)  # Go down

        generate_path(i, j, distances[i][j])
        for line in self.matrix:
            print(' '.join(line))
        return "\n Complete."


str = """sxoxoooo
oxoooxxo
ooxoxooo
xoooxoxo
oxoxooxo
oooxoxoo
oxxxoxox
ooxooxoe"""

test_maze = Maze(str)
print(test_maze.solve_maze())
