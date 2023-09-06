'''
Lightweight image viewer to test out if I can get it to work and how quick it can be.

Henry Hall 8/22/23
'''

import glob
import PySimpleGUI as sg
from PIL import Image, ImageTk
import image_flipper

def parse_folder(path):
    images = glob.glob(f'{path}/*.jpg') + glob.glob(f'{path}/*.png') + glob.glob(f'{path}/*.tif')
    return images

def load_image(path, window):
    try:
        image = Image.open(path)
        image.thumbnail((500, 500))
        photo_img = ImageTk.PhotoImage(image)
        window["image"].update(data=photo_img)
    except:
        print(f"Unable to open {path}!")
        
def main():
    elements = [
        [sg.Image(key="image")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), enable_events=True, key="file"),
            sg.FolderBrowse(),
        ],
        [
            sg.Button("Prev"),
            sg.Button("Next"),
            sg.Button('Turn Left'),
            sg.Button('Flip'),
            sg.Button('Turn Right')
        ]
    ]
    window = sg.Window("Image Viewer", elements, size=(600, 600))
    images = []
    location = 0
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "file":
            images = parse_folder(values["file"])
            if images:
                load_image(images[0], window)
        if event == "Next" and images:
            if location == len(images) - 1:
                location = 0
            else:
                location += 1
            load_image(images[location], window)
        if event == "Prev" and images:
            if location == 0:
                location = len(images) - 1
            else:
                location -= 1
            load_image(images[location], window)
        if event == "Flip" and images:
            image_flipper.flip_file(images[location])
            load_image(images[location], window)
        if event == 'Turn Left' and images:
            image_flipper.turn_left(images[location])
            load_image(images[location],window)
        if event == 'Turn Right' and images:
            image_flipper.turn_right(images[location])
            load_image(images[location],window)
    window.close()

if __name__ == "__main__":
    main()