from tkinter import *
import PIL.Image
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def make_point(self, canvas):
        point = canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill="blue")
        return point
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def make_line(self, canvas):
        line = canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black", width=2)
        return line
class GUI:
    def __init__(self, root, img):
        self.img = img
        self.root = root
        self.w, self.h = PIL.Image.open(self.img).size
        self.img = PhotoImage(file=self.img)
        self.current_point = {"name": None, "point": None, "x": None, "y": None, "linesname":None, "lines": None}
        
       
        self.canvas = Canvas(self.root, width=self.w, height=self.h, bg= "white")
        self.canvas.pack(pady=40)
        self.canvas.create_image(self.w/2, self.h/2, image=self.img)
        
        self.quadrilateral_corners = self.quadrilateral(self.w/2, self.h/2, self.canvas)
        print(self.quadrilateral_corners)
        self.quadrilateral_shape = self.draw_line(self.quadrilateral_corners["names"], self.canvas)
        print(self.quadrilateral_shape)
        self.coords_label = Label(self.root, width=int(self.w/2), height=self.h, text="Press anywhere for Coordinates")
        self.coords_label.pack()
        
        self.canvas.bind("<ButtonPress-1>", self.OnPress)
        self.canvas.bind("<B1-Motion>", self.OnDrag)
        self.canvas.bind("<ButtonRelease-1>", self.OnRelease)
    def OnPress(self, event):
        closest_point = None
        min_distance = 13.5  # Set initial distance to infinity
        i = 0
        for i, point in enumerate(self.quadrilateral_corners["names"]):  # Iterate through points
            distance = ((point.x - event.x)**2 + (point.y - event.y)**2)**0.5  # Calculate distance
            if distance < min_distance:
                min_distance = distance
                closest_point = self.quadrilateral_corners["points"][i]
                closest_name = point
                self.current_point["point"] = closest_point# Store the Point object
                self.current_point["name"] = closest_name
                self.current_point["x"] = event.x
                self.current_point["y"] = event.y
                self.current_point["linesname"] = self.quadrilateral_shape["names"][i]
                self.current_point["lines"] = self.quadrilateral_shape["lines"][i]
                print(self.current_point)
        
    def OnRelease(self, event):
        self.current_point["name"] = None
        self.current_point["point"] = None
        self.current_point["x"] = None
        self.current_point["y"] = None
        self.current_point["linesname"] = None
        self.current_point["lines"] = None
    def OnDrag(self, event):
        self.coords_label.config(text=f"Coordinate: x:{str(event.x)}, y:{str(event.y)}")
        if self.current_point["name"] != None:
            self.canvas.coords(self.current_point["point"], event.x - 5, event.y - 5, event.x + 5, event.y + 5)
            self.current_point["name"].x = event.x
            self.current_point["name"].y = event.y
            match self.current_point["point"]:
                case n if n in [2, 5]:#1
                    x_coord_2 = self.quadrilateral_corners["names"][1].x
                    y_coord_2 = self.quadrilateral_corners["names"][1].y
                    self.canvas.coords(self.current_point["lines"][0], x_coord_2, y_coord_2, event.x, event.y)
                    x_coord_3 = self.quadrilateral_corners["names"][2].x
                    y_coord_3 = self.quadrilateral_corners["names"][2].y
                    self.canvas.coords(self.current_point["lines"][1], x_coord_3, y_coord_3, event.x, event.y)
                case m if m in [3, 4]:#1
                    x_coord_1 = self.quadrilateral_corners["names"][0].x
                    y_coord_1 = self.quadrilateral_corners["names"][0].y
                    self.canvas.coords(self.current_point["lines"][0], x_coord_1, y_coord_1, event.x, event.y)
                    x_coord_4 = self.quadrilateral_corners["names"][3].x
                    y_coord_4 = self.quadrilateral_corners["names"][3].y
                    self.canvas.coords(self.current_point["lines"][1], x_coord_4, y_coord_4, event.x, event.y)
                

    def quadrilateral(self, x, y, canvas):
        point_1 = Point(x - 100, y - 100)
        p1 = point_1.make_point(canvas)
        point_2 = Point(x + 100, y - 100)
        p2 = point_2.make_point(canvas)
        point_3 = Point(x - 100, y + 100)
        p3 = point_3.make_point(canvas)
        point_4 = Point(x + 100, y + 100)
        p4 = point_4.make_point(canvas)
        return {"names": [point_1, point_2, point_3, point_4], "points": [p1, p2, p3, p4]}
    def draw_line(self, point_names: list, canvas):
        point_1, point_2, point_3, point_4 = point_names
        line_1_2 = Line(point_1.x, point_1.y, point_2.x, point_2.y)
        l12 = line_1_2.make_line(self.canvas)
        line_1_3 = Line(point_1.x, point_1.y, point_3.x, point_3.y)
        l13 = line_1_3.make_line(self.canvas)
        line_4_2 = Line(point_4.x, point_4.y, point_2.x, point_2.y)
        l42 = line_4_2.make_line(self.canvas)
        line_4_3 = Line(point_4.x, point_4.y, point_3.x, point_3.y)
        l43 = line_4_3.make_line(self.canvas)
        return {"names":[(line_1_2, line_1_3), (line_1_2, line_4_2), (line_1_3, line_4_3), (line_4_2, line_4_3)],
                "lines":[(l12, l13), (l12, l42), (l13, l43), (l42, l43)]}

if __name__ == "__main__":
    root = Tk()
    img = "inputs/ori.png"
    gui = GUI(root, img)
    img = PIL.Image.open(img)
    w, h = img.size
    root.geometry(f"{w + 200}x{h + 200}")
    root.mainloop()
    coords =gui.quadrilateral_corners["names"]
    x1, y1 = coords[0].x, coords[0].y
    x2, y2 = coords[1].x, coords[1].y
    x3, y3 = coords[2].x, coords[2].y
    x4, y4 = coords[3].x, coords[3].y
    print((x1, y1), (x2, y2), (x3, y3), (x4, y4))
    