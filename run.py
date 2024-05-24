import cv2
import PIL.Image
from tkinter import *
from GUI_drag import GUI
from perwarp import warp_perspective

def main():
    height = 204
    width = 323
    
    root = Tk()
    img = "inputs/ori.png"
    gui = GUI(root, img)
    img = PIL.Image.open(img)
    w, h = img.size
    root.geometry(f"{w + 100}x{h + 100}")
    root.mainloop()
    coords = gui.quadrilateral_corners["names"]
    
    
    image = cv2.imread("inputs/ori.png")
    new_image = warp_perspective(image, coords, width, height)
    cv2.imshow("new_image", new_image)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
    cv2.imwrite("saves/new_image.png", new_image)
    image = cv2.imread("inputs/ori.png")
if __name__ == "__main__":
    main()