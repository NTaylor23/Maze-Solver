import copy

def create_matrix(m_string: list[list]) -> str:
    """ used to create a console-friendly string version of the maze

    Args:
        m_string (list[list]): the current maze, as a list

    Returns:
        str: maze as string, with each row separated by new line characters
    """
    res = []
    for line in m_string:
        res.append(list(line))
    return res

class Maze:

    def __init__(self, matrix_import: list[list], begin: tuple, end: tuple):
        self.matrix = matrix_import
        self.width, self.height = self.find_width_height()
        self.heatmap = None
        self.max_value = 0
        self.begin, self.end = begin, end

    def find_width_height(self):
        return [len(self.matrix[0]), len(self.matrix)]

    def out_of_bounds(self, ver: int, hor: int, visited: set) -> bool:
        """ checks if a point is in range, checks if a point has been visited,
        then returns a value of True if the point is in-range and unvisited

        Args:
            ver (int): y value
            hor (int): x value
            visited (set): hash set of visited points

        Returns:
            bool: _description_
        """
        if ver not in range(0, self.height) or hor not in range(0, self.width):
            return True
        elif (ver, hor) in visited:
            return True
        elif self.matrix[ver][hor] == 'x':
            return True
        return False

    def solve_maze(self) -> None:
        """ delegator function for flood-fill/BFS operations """
        i, j = self.end
        visited = set()
        matrix_copy = copy.deepcopy(self.matrix)

        def flood_fill(y: int, x: int, grid: list[list], dist: int) -> list[list]:
            """_summary_

            Args:
                ver (int): y value
                hor (int): x value
                grid (list[list]): grid represented as list of lists
                dist (int): distance from current point to start point

            Returns:
                list[list]: grid with distance values for each reachable point
            """
            if self.out_of_bounds(y, x, visited) or self.matrix[y][x] == 's':
                return
            
            visited.add((y, x))
            grid[y][x] = dist
            dist += 1

            flood_fill(y, x - 1, grid, dist)  # Go left
            flood_fill(y, x + 1, grid, dist)  # Go right
            flood_fill(y - 1, x, grid, dist)  # Go up
            flood_fill(y + 1, x, grid, dist)  # Go down

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

        def generate_path(ver_hor_distance: tuple) -> list[list]:
            """_summary_

            Args:
                ver_hor_distance (tuple): y value, x value, distance value

            Returns:
                list[list]: the solved maze
            """
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

