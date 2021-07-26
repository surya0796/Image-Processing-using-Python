import sys
import os
from PIL import Image

image_folder = sys.argv[1] +'\\'

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


output_folder = desktop +"\\"+ sys.argv[2] + '\\'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for file in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{file}') 
    clean_name = os.path.splitext(file)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print("all done!")