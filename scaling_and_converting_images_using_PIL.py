#!/usr/bin/env python3

import os
import glob
from PIL import Image


# Directory containing the images
image_directory = 'images'
# Directory where the modified images will be saved
output_directory = '/opt/icons/'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through each file in the image directory
for filename in os.listdir(image_directory):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        # Construct the full file path
        file_path = os.path.join(image_directory, filename)
        # Open the image
        with Image.open(file_path) as img:
            # Rotate and resize the image
            modified_img = img.rotate(270, expand=True).resize((128, 128))
            # Construct the output file path
            output_file_path = os.path.join(output_directory, os.path.splitext(filename)[0] + '.jpeg')
            # Save the modified image
            modified_img.save(output_file_path, 'JPEG')

print("Image processing complete.")
