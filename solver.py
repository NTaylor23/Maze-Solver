import copy

def create_matrix(m_string):
    res = []
    for line in m_string:
        res.append(list(line))
    return res

class Maze:
    def __init__(self, matrix_import, begin, end):
        self.matrix = matrix_import
        self.width, self.height = self.find_width_height()
        self.begin, self.end = begin, end

    def find_width_height(self):
        return [len(self.matrix[0]), len(self.matrix)]

    def out_of_bounds(self, ver, hor, visited):
        if ver not in range(0, self.height) or hor not in range(0, self.width):
            return True
        elif (ver, hor) in visited:
            return True
        elif self.matrix[ver][hor] == 'x':
            return True
        return False

    def solve_maze(self):
        begin, finish = self.begin, self.end
        i, j = finish
        visited = set()
        matrix_copy = copy.deepcopy(self.matrix)

        def flood_fill(ver, hor, grid, dist):
            if self.out_of_bounds(ver, hor, visited) or self.matrix[ver][hor] == 's':
                return
            visited.add((ver, hor))
            grid[ver][hor] = dist
            dist += 1

            flood_fill(ver, hor - 1, grid, dist)  # Go left
            flood_fill(ver, hor + 1, grid, dist)  # Go right
            flood_fill(ver - 1, hor, grid, dist)  # Go up
            flood_fill(ver + 1, hor, grid, dist)  # Go down

            return grid

        numeric_grid = flood_fill(i, j, matrix_copy, 0)
        i, j = self.begin
        visited.clear()

        def generate_path(ver, hor, distance):
            if self.out_of_bounds(ver, hor, visited) or numeric_grid[ver][hor] > distance:
                return

            if numeric_grid[ver][hor] == 0:
                self.matrix[ver][hor] = '.'
                return self.matrix

            visited.add((ver, hor))
            self.matrix[ver][hor] = '.'
            loc = numeric_grid[ver][hor]

            generate_path(ver, hor - 1, loc)  # Go left
            generate_path(ver, hor + 1, loc)  # Go right
            generate_path(ver - 1, hor, loc)  # Go up
            generate_path(ver + 1, hor, loc)  # Go down

        generate_path(i, j, numeric_grid[i][j])
        return self.matrix
