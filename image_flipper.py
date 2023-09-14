'''
Image flipper to flip a single file.
'''

from pathlib import Path
from PIL import Image
import os, stat

def change_permissions(file_path):
    '''
    Changes permssions of the file at the path.

    param file_path: path to the file that you want to be able to write to.
    '''
    os.chmod(file_path,stat.S_IWRITE)

def flip_file(file_path):
    '''
    Flips an image file.

    param file_path: path to the file to flip.

    returns bool. True if it works.
    '''
    change_permissions(file_path)
    try:
        with Image.open(file_path) as im:
            im = im.transpose(3)
            im.save(file_path)
            return True
    except:
        print('Could not flip file')
        return False
    
def turn_left(file_path):
    '''
    Turns an image file left 90 degrees.

    param file_path: path to the file to turn.

    returns bool. True if it works
    '''
    change_permissions(file_path)
    try:
        with Image.open(file_path) as im:
            im = im.transpose(2)
            im.save(file_path)
            return True
    except:
        print('Could not turn file')
        return False
    
def turn_right(file_path):
    '''
    Turns an image file left 90 degrees.

    param file_path: path to the file to turn.

    returns bool. True if it works.
    '''
    change_permissions(file_path)
    try:
        with Image.open(file_path) as im:
            im = im.transpose(4)
            im.save(file_path)
            return True
    except:
        print('Could not turn file')
        return False
    
def correct_orientation(file_path):
    '''
    Corrects an image's orientation.

    Kind of a hack, since I'm just going to rotate it 360 degrees, but it's easier than changing image attributes.

    param file_path: path to the file to correct orientation for.

    returns None
    '''
    change_permissions(file_path)
    try:
        with Image.open(file_path) as im:
            im = im.rotate(360)
            im.save(file_path)
    except:
        print('Could not correct file orientation.')

def test_losslessness(file_path, times_to_test = 1000):
    '''
    For testing how many times I can open, rotate, and save an image.

    param file_path: path to the image to test on.
    param times_to_test: integer for how many times to turn save.

    returns None
    '''
    for i in range(0, times_to_test):
        with Image.open(file_path) as im:
            im = im.rotate(90)
            im.save(file_path)