from tkinter import *
class GUI:
    def __init__(self, root, width= 1280, height= 720):
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=self.width, height=self.height)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    