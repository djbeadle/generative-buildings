from canvas import *
from math import sin, cos, pi

def draw_half(x_midpoint=300, x_width=150, slope=0.2, y_edge=300, side="left", color=(1, 0.5, 0.2)):
    if side == "left":
        x_delta = -x_width
    else:
        x_delta = x_width
        
    y_peak = slope * (x_midpoint - (x_midpoint - x_width)) + y_edge
        
    add_line(x_midpoint + x_delta, 0)
    add_line(x_midpoint + x_delta, y_edge)
    add_line(x_midpoint, y_peak)
    add_line(x_midpoint, 0)
    add_line(x_midpoint + x_delta, 0)
    close_path()
    set_fill_color(*color)
    fill_path()

def draw_window(x_mid, y_mid, slope, height, width):
    begin_path()
    set_line_width(2)
    set_stroke_color(0.5,0.5,0.5)
    top_right = (x_mid + width, y_mid + height)
    top_left = (x_mid - width, slope * ((x_mid-width)-(x_mid+width))+(y_mid+height))
    
    bottom_left = (x_mid - width, y_mid - height)
    bottom_right = (x_mid + width, slope * ((x_mid+width)-(x_mid-width))+(y_mid-height))
    print(top_right)
    print(top_left)
    move_to(*top_right)
    add_line(*top_left)
    add_line(*bottom_left)
    add_line(*bottom_right)
    
    close_path()
    fill_path()
    


w = 600
h = 600
slope = 0.4
set_size(w, h)

draw_half(side="left", slope=slope, color=(1, 0.5, 0.2))
move_to(0, 0)
draw_half(side="right", slope=slope, color=(0.9, 0.5, 0.2))

draw_window(225, 225, 0.4, 40, 20)
