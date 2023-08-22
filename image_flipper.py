'''
Image flipper to flip a single file.
'''

from pathlib import Path
from PIL import Image
import os

def flip_file(file_path):
    '''
    Flips an image file.

    param file_path: path to the file to flip.

    returns bool. True if it works.
    '''
    try:
        with Image.open(file_path) as im:
            im = im.transpose(3)
            im.save(file_path)
            return True
    except:
        print('Could not flip file')
        return False