class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_point(self, canvas):
        point = canvas.create_oval(self.x - 3, self.y - 3, self.x + 3, self.y + 3, fill="red")
        return point

import PIL.Image
from tkinter import *

def on_drag(event):
    coords_label.config(text=f"Coordinate: x:{str(event.x)}, y:{str(event.y)}")
    if current_point["name"] != None:
        canvas.coords(current_point["point"], event.x - 3, event.y - 3, event.x + 3, event.y + 3)
        current_point["name"].x = event.x
        current_point["name"].y = event.y

img = PIL.Image.open("inputs/unwarp.jpg")
w, h = img.size
x, y = w / 2, h / 2
root = Tk()
root.title("GUI_TEST")
root.geometry(f"{w + 100}x{h + 100}")

current_point = {"name": None, "point": None, "x": None, "y": None}

canvas = Canvas(root, width=w, height=h)
img = PhotoImage(file="saves/ori.png")
image = canvas.create_image(x, y, image=img)
point_1 = Point(x - 100, y - 100)
p1 = point_1.make_point(canvas)
point_2 = Point(x + 100, y - 100)
p2 = point_2.make_point(canvas)
point_3 = Point(x - 100, y + 100)
p3 = point_3.make_point(canvas)
point_4 = Point(x + 100, y + 100)
p4 = point_4.make_point(canvas)

def OnCircleButtonPress(event):
    closest_point = None
    min_distance = 13.5  # Set initial distance to infinity
    i = 0
    for point in [point_1, point_2, point_3, point_4]:  # Iterate through points
        distance = ((point.x - event.x)**2 + (point.y - event.y)**2)**0.5  # Calculate distance
        if distance < min_distance:
            min_distance = distance
            closest_point = eval(f"p{i+1}")
            closest_name = point
        i += 1
    if closest_point:
        current_point["point"] = closest_point# Store the Point object
        current_point["name"] = closest_name
        current_point["x"] = event.x
        current_point["y"] = event.y
    else:
        current_point["point"] = None  # No point clicked
    print(current_point)

def OnCircleButtonRelease(event):
    current_point["x"] = None
    current_point["y"] = None

canvas.pack(pady=20)
coords_label = Label(root, width=int(x), height=h, text="Coordinates")
canvas.bind("<ButtonPress-1>", OnCircleButtonPress)
canvas.bind("<ButtonRelease-1>", OnCircleButtonRelease)
canvas.bind("<B1-Motion>", on_drag)
coords_label.pack()

root.mainloop()