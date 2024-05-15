import PIL.Image
from tkinter import *

def drag(event):
    canvas.coords(image, event.x, event.y)
    canvas.itemconfig(text, text=f"Coordinate: x:{str(event.x)}, y:{str(event.y)}")
    
    
img = PIL.Image.open("inputs/unwarp.jpg")
w, h = img.size
x, y = w/2, h/2
root = Tk()
root.title("GUI_TEST")
root.geometry(f"{w}x{h}")

#Make black canvas, which is the place where objects are drawn
canvas = Canvas(root, width=w, height=h, bg= "white")
img = PhotoImage(file="saves/new_image.png")
image = canvas.create_image(x, y, image= img)
text = canvas.create_text(300, 50, text="Drag for Coords", fill="black", font=('Helvetica 15 bold'))
canvas.pack(pady= 20)
canvas.bind("<B1-Motion>", drag)

root.mainloop()