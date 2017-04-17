import collatz_visual
import math
import numpy as np
from tqdm import tqdm

def create_animation():
    count = 0
    for i in tqdm(np.arange(1,20,.1)):
        collatz_visual.draw(size=800,line_length=7,turn=i,maximum=20000,tk=False,image=True,filename="animation_ip/s"+str(count))
        count += 1

def create_image():
    collatz_visual.draw(size=800,line_length=7,turn=20,maximum=100,tk=False,image=True)

def create_3d_scatter():
    # stuff
    pass