import copy
import itertools


def create_matrix(m_string):
    res = []
    for line in m_string:
        res.append(list(line))
    return res

class Maze:
    def __init__(self, matrix_import, begin, end):
        self.matrix = matrix_import
        self.width, self.height = self.find_width_height()
        self.heatmap = None
        self.max_value = 0
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

    def set_heatmap(self, heatmap):
        self.heatmap = heatmap

    def get_heatmap(self):
        return self.heatmap

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
        for line in numeric_grid:
            print(list(map(str, line)))
        max = 0
        for line in numeric_grid.copy():
            for element in line:
                if element in range(0, 1000) and element > max:
                    max = element
        self.max_value = max
        self.heatmap = numeric_grid.copy()
        i, j = self.begin
        visited.clear()

        def generate_path(ver_hor_distance):
            if not ver_hor_distance:
                return self.matrix
            else:
                x = ver_hor_distance.pop(0)
                print(x)
                ver, hor, distance = x

                if numeric_grid[ver][hor] == 0:
                    self.matrix[ver][hor] = '.'
                    return self.matrix

                visited.add((ver, hor))
                self.matrix[ver][hor] = '.'
                loc = numeric_grid[ver][hor]

                if self.out_of_bounds(ver, hor - 1, visited) or numeric_grid[ver][hor] > distance:
                    ver_hor_distance += [[ver, hor - 1, loc], [ver, hor + 1, loc], [ver - 1, hor, loc], [ver + 1, hor, loc]]

                generate_path(ver_hor_distance)

        generate_path([[i, j, numeric_grid[i][j]]])
        for line in self.matrix:
            print(''.join(line))
        return self.matrix

    def return_matrix(self):
        return self.matrix

