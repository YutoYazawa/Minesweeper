import numpy as np
import pygame
from colors import *


def on_area(left_up_coord,right_down_coord,click_coord):
    if left_up_coord[0]<click_coord[0] and click_coord[0]<right_down_coord[0] and left_up_coord[1]<click_coord[1] and click_coord[1]<right_down_coord[1]:
        return True
    else:
        return False

def draw_flag(screen, coord, cell_size):
    pygame.draw.line(screen,FLAG,(coord[0]+4,coord[1]+4),(coord[0]+4,coord[1]+cell_size[1]-4))
    pygame.draw.polygon(screen,FLAG,[(coord[0]+4,coord[1]+4),(coord[0]+4+cell_size[1]/4*3,coord[1]+cell_size[1]/4),(coord[0]+4,coord[1]+cell_size[1]/2)])