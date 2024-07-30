import cv2
import PIL.Image
from tkinter import *
from GUI_drag import GUI
from perwarp import warp_perspective
from pre_edit import ImageRotator
import tkinter.messagebox as messagebox
import sys, os


def main():
    height = 382
    width = 606

    root_1 = Tk()
    root_1.title("Image Rotator")
    app = ImageRotator(root_1)
    root_1.mainloop()
    path = app.path

    if not path:
        messagebox.showerror("Error", "No Image Found.")
        sys.exit("No Image Found")

    root_2 = Tk()
    gui = GUI(root_2, path)
    img = PIL.Image.open(path)
    w, h = img.size
    root_2.geometry(f"{w + 100}x{h + 100}")
    root_2.mainloop()
    coords = gui.quadrilateral_corners["names"]

    image = cv2.imread(path)
    new_image = warp_perspective(image, coords, width, height)
    cv2.imshow("new_image", new_image)
    # Auto close after 3 seconds
    key = cv2.waitKey(3000)
    if key == 27:
        cv2.destroyAllWindows()
    cv2.imwrite(f"saves/" + app.extension, new_image)
    os.remove(path)


if __name__ == "__main__":
    main()
