import tkinter as tk
from PIL import Image
from PIL import ImageDraw
import collatz_calculator as cc
import collatz_data
import math

LINE_LENGTH = 3
SIZE = 700
MAXIMUM = 10000
TURN = 40

TK = True
IMAGE = False

top = None

C = None
center = None

def init_tk():
    global top, C

    top = tk.Tk()
    C = tk.Canvas(top,bg="black",height=SIZE,width=SIZE)

IMG = None
DRAW = None
white = (255, 255, 255)
black = (0, 0, 0)

def init_image():
    global IMG, DRAW
    # PIL create an empty image and draw object to draw on
    # memory only, not visible
    IMG = Image.new("RGB", (SIZE, SIZE), black)
    DRAW = ImageDraw.Draw(IMG)


data = None

def get_next_loc(prev,d,angle):
    if d < 0:
        t = TURN
    else:
        t = -TURN

    angle += t

    return [
        [
            prev[0]+(LINE_LENGTH*math.cos(angle)),
            prev[1]+(LINE_LENGTH*math.sin(angle))
        ],
        angle
    ]

def draw_path(prev,child,angle=math.pi/2):
    
    parents = data[child]

    for p in parents:
        # negative if did 3n-1, positive if did n/2
        result = get_next_loc(prev,p-child,angle)
        new = result[0]
        a = result[1]

        if TK:
            C.create_line(prev[0],prev[1],new[0],new[1],fill="white")
        if IMAGE:
            DRAW.line([prev[0],prev[1],new[0],new[1]],white)

        if p in data and p < MAXIMUM:
            draw_path(new,p,angle=a)

def draw(start=None,line_length=LINE_LENGTH,size=SIZE,maximum=MAXIMUM,turn=TURN,tk=TK,image=IMAGE):
    global data, LINE_LENGTH, SIZE, center, MAXIMUM, TURN, TK, IMAGE

    data = collatz_data.read()

    LINE_LENGTH = line_length
    SIZE = size
    center = [SIZE//2,SIZE//2]
    MAXIMUM = maximum
    TURN = math.pi/turn
    TK = tk
    IMAGE = image

    if TK:
        init_tk()
    if IMAGE:
        init_image()

    if start == None:
        start = center

    draw_path(start,1)

    if TK:
        C.pack()
        top.mainloop()
    if IMAGE:
        IMG.save("visuals/collatz_visual_" + str(MAXIMUM) + ".jpg")