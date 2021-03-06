# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:59:30 2020

@author: Nika
"""
import numpy as np
import pygame as pg
from random import randint
import physics


BLACK = (0, 0, 0)
LSALMON = (255, 160, 122)
PEACH = (255, 218, 185)
LEMONE = (255, 250, 205)
SKYBLUE = (100, 149, 237)
TOMATO = (255, 99, 71)
CADET = (176, 196, 222)
SLATE = (106, 90, 205)
DARK = (72, 61, 109)
BROWN = (139, 69, 19)
GREY = (130, 130, 130)
COLORS = [LSALMON, PEACH, LEMONE, SKYBLUE, TOMATO, GREY, CADET, BROWN]

pg.init()

class Body():
    def __init__(self, mass, coord, vel, rad, color=None):
        self.mass = mass
        self.coord = coord
        self.rad = rad
        self.vel = vel
        if color == None:
            color = COLORS[randint(0,len(COLORS)-1)]
            
    def move():
        physics.acceleration()
    
    def draw():
        pass

