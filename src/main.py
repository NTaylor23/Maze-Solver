import reader
import solver
import writer
import sys
"""
To optimize the flood-fill/DFS:
- Instead of going by pixel by pixel, calculate the size of the opening, 
and use that to compute a square area that can act as a square, which becomes the object that
moves through the maze.
- The clump of pixels will have to have its distance from the end represented somehow. 
Maybe choose the point at the topmost row and the middle column.

General improvements:
- Detect openings on the sides, not just the top and bottom.

Start itself should be red
The longer the distance from the end, the color should turn to blue
"""

def draw_shortest_path(blank_maze_image_path, processed_maze_image_path):
    maze_reader = reader.ProcessImage(blank_maze_image_path)

    matrix = maze_reader.conv_matrix()
    start = maze_reader.start
    end = maze_reader.end

    maze_init = solver.Maze(matrix, start, end)
    maze_init.solve_maze()
    result_init = maze_init.matrix
    max_value = maze_init.max_value
    heatmap = maze_init.heatmap
    writer.WriteImage(result_init, heatmap, max_value).create_image(processed_maze_image_path)

# if __name__ == '__main__':
#     print('\033[93m' + "Nothing in main")

in_path, out_path = sys.argv[1:]
draw_shortest_path(in_path, out_path)