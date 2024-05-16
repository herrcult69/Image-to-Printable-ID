from tkinter import *
import PIL.Image
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def make_point(self, canvas):
        point = canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill="blue")
        return point

class GUI:
    def __init__(self, root, img):
        self.img = img
        self.root = root
        self.w, self.h = PIL.Image.open(self.img).size
        self.img = PhotoImage(file=self.img)
        self.current_point = {"name": None, "point": None, "x": None, "y": None}
        
       
        self.canvas = Canvas(self.root, width=self.w, height=self.h)
        self.canvas.pack(pady=20)
        self.canvas.create_image(self.w/2, self.h/2, image=self.img)
        
        self.quadrilateral_shape = self.quadrilateral(self.w/2, self.h/2)
        
        self.coords_label = Label(self.root, width=int(self.w/2), height=self.h, text="Press anywhere for Coordinates")
        self.coords_label.pack()
        
        self.canvas.bind("<ButtonPress-1>", self.OnPress)
        self.canvas.bind("<ButtonRelease-1>", self.OnRelease)
        self.canvas.bind("<B1-Motion>", self.OnDrag)
    def OnPress(self, event):
        closest_point = None
        min_distance = 13.5  # Set initial distance to infinity
        i = 0
        for point in self.quadrilateral_shape["names"]:  # Iterate through points
            distance = ((point.x - event.x)**2 + (point.y - event.y)**2)**0.5  # Calculate distance
            if distance < min_distance:
                min_distance = distance
                closest_point = self.quadrilateral_shape["points"][i]
                closest_name = point
            i += 1
        if closest_point:
            self.current_point["point"] = closest_point# Store the Point object
            self.current_point["name"] = closest_name
            self.current_point["x"] = event.x
            self.current_point["y"] = event.y
        else:
            self.current_point["point"] = None  # No point clicked
    def OnRelease(self, event):
        self.current_point["name"] = None
        self.current_point["point"] = None
        self.current_point["x"] = None
        self.current_point["y"] = None
    def OnDrag(self, event):
        self.coords_label.config(text=f"Coordinate: x:{str(event.x)}, y:{str(event.y)}")
        if self.current_point["name"] != None:
            self.canvas.coords(self.current_point["point"], event.x - 5, event.y - 5, event.x + 5, event.y + 5)
            self.current_point["name"].x = event.x
            self.current_point["name"].y = event.y

    def quadrilateral(self, x, y):
        point_1 = Point(x - 100, y - 100)
        p1 = point_1.make_point(self.canvas)
        point_2 = Point(x + 100, y - 100)
        p2 = point_2.make_point(self.canvas)
        point_3 = Point(x - 100, y + 100)
        p3 = point_3.make_point(self.canvas)
        point_4 = Point(x + 100, y + 100)
        p4 = point_4.make_point(self.canvas)
        return {"names": [point_1, point_2, point_3, point_4], "points": [p1, p2, p3, p4]}

if __name__ == "__main__":
    root = Tk()
    img = "inputs/ori.png"
    gui = GUI(root, img)
    img = PIL.Image.open(img)
    w, h = img.size
    root.geometry(f"{w + 100}x{h + 100}")
    root.mainloop()
    coords =gui.quadrilateral_shape["names"]
    x1, y1 = coords[0].x, coords[0].y
    x2, y2 = coords[1].x, coords[1].y
    x3, y3 = coords[2].x, coords[2].y
    x4, y4 = coords[3].x, coords[3].y
    print((x1, y1), (x2, y2), (x3, y3), (x4, y4))
    