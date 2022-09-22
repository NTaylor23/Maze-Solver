import main
import cv2
import uuid
import os
import shutil

path_to_output_directory = 'assets/test_resources/output'
path_to_blank_maze = 'assets/test_resources/verysmall.png'
path_to_completed_maze = 'assets/test_resources/maze_completed.png'

try:
    name = uuid.uuid4()
    path_to_new_image = f'{path_to_output_directory}/{name}.png'

    main.draw_shortest_path(path_to_blank_maze, path_to_new_image)

    original = cv2.imread(path_to_completed_maze)
    processed = cv2.imread(path_to_new_image)

    if original.shape == processed.shape:
        print('Same size.')

    difference = cv2.subtract(original, processed)
    b, g, r = cv2.split(difference)
    print(b, g, r)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print('\033[92m' + 'Images are equal.')
    else:
        print('\033[91m' + 'Images are NOT equal.')

except Exception as e:
    raise e

# finally:
#     # shutil.rmtree(path_to_output_directory)
#     # os.mkdir(path_to_output_directory)