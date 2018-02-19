# This class defines a table that is 2D square that is a play area.

from tkinter import *

class Table:
    #### constructor
    def __init__(self, window, color="black", net_color="white", width=1000, height=1000, vertical_net=False, horizontal_net=False):
        self.width = width
        self.height = height
        self.color = color
# order a canvas to draw on frm the tkinter factory:
        self.canvas = Canvas(window, bg=self.color, height=self.height, width=self.width)
        self.canvas.pack()

# add a net to the canvas using a method from the tkinter factory:
        if(vertical_net):
            self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, fill=net_colour, dash=(15,23))
                       
        if(horizontal_net):
            self.canvas.create_line(0, self.height/2, self.width, self.height/2, width=2, fill=net_colour, dash=(15,23))

# extra tool for adding a rectangle to the canvas:
    def draw_square(self, square):
        x1 = square.x_posn
        x2 = square.x_posn + square.width
        y1 = square.y_posn
        y2 = square.y_posn + square.height
        c = square.color
        return self.canvas.create_square(x1, y1, x2, y2, fill=c)
