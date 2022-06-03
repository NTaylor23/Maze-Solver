import reader
import solver
import writer

"""
To optimize the flood-fill/DFS:
- Instead of going by pixel by pixel (what the fuck?), calculate the size of the opening, 
and use that to compute a square area that can act as a square, which becomes the object that
moves through the maze.
- The clump of pixels will have to have its distance from the end represented somehow. 
Maybe choose the point at the topmost row and the middle column.

General improvements:
- Detect openings on the sides, not just the top and bottom.
"""

def main():
    maze_reader = reader.ProcessImage('assets/maze.png')

    matrix = maze_reader.conv_matrix()
    start = maze_reader.start
    end = maze_reader.end

    result_init = solver.Maze(matrix, start, end).solve_maze()
    pic = writer.WriteImage(result_init).create_image()


if __name__ == '__main__':
    main()
