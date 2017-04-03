import tkinter as tk
import collatz_calculator as cc
import math

line_length = 1
size = 700
maximum = 10000000
turn = math.pi/55

top = tk.Tk()

C = tk.Canvas(top,bg="black",height=size,width=size)
center = [size//2,size//2]
start = center

# C.create_line(0,0,50,50,fill="white")

cc.generate_tree(1,maximum)

def get_next_loc(prev,d,angle):
    if d < 0:
        t = turn
    else:
        t = -turn

    angle += t

    return [
        [
            prev[0]+(line_length*math.cos(angle)),
            prev[1]+(line_length*math.sin(angle))
        ],
        angle
    ]

def draw_path(prev,child,angle=math.pi/2):
    
    parents = cc.tree[child]

    for p in parents:
        # negative if did 3n-1, positive if did n/2
        result = get_next_loc(prev,p-child,angle)
        new = result[0]
        a = result[1]

        C.create_line(prev[0],prev[1],new[0],new[1],fill="white")
        if p in cc.tree:
            draw_path(new,p,angle=a)

draw_path(start,1)

C.pack()
top.mainloop()