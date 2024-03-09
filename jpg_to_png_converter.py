import sys
import os
from PIL import Image

# get two arguments passed by user
if len(sys.argv) != 3:
    print("Usage: python scriptname.py images_directory output_directory")
    exit()
else:
    image_directory = sys.argv[1]  # the name of the input image file
    output_directory = sys.argv[2]  # the name of the output directory

# check if the specified output directory exists, otherwise create it
if not os.path.exists(output_directory):
    try:
        # make a new directory because it does not exist
        os.makedirs(output_directory)
    except OSError as e:
        print('An error occurred creating the directory:\n', e)
        exit()

for filename in os.listdir(image_directory):
    try:
        img = Image.open(f'{image_directory}{filename}')  # open an image file
    except IOError as e:
        print('An error occurred trying to read the image file:\n', e)
        exit()

    # Get filename without extension
    base_filename = os.path.splitext(filename)[0]

    img.save(f'{output_directory}{base_filename}.png', 'png')  # save the image


print('All done!')
