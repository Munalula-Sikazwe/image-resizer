from PIL import Image
from pathlib import Path
from argparse import ArgumentParser
import os

directories = ArgumentParser(description='Directories that can be used to store the images')

directories.add_argument('image_dir',
                        metavar='Image_dir',
                        type=str,
                        help='The path to the image folder'
                            )
directories.add_argument('save_dir',
                        metavar='Save_dir',
                        type=str,
                        help='The path to the image save folder'
                            )

args = directories.parse_args()

input_path = args.image_dir
output_path = args.save_dir

if not os.path.exists(output_path):
    os.makedirs(output_path)
def process_images(input_path,output_path=output_path):
    for filename in os.listdir(input_path):
        fullpath = os.path.join(input_path,filename)
        if os.path.isfile(fullpath):
            clean_name = os.path.splitext(filename)[0]
            img = Image.open(f'{input_path}{filename}')
            img = img.resize((600,338))
            img.save(f'{output_path}/{clean_name}.jpeg', 'jpeg')
            print('all done!')
        else:
            if os.path.isdir(fullpath):
                fullpath = fullpath + '/'
                process_images(fullpath,output_path=output_path)

process_images(input_path,output_path)
