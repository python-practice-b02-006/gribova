# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:34:28 2020

@author: Nika
"""
import numpy as np
import pygame as pg
from random import randint, gauss

SIZE = (600, 600)
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
COLORS = [LSALMON, PEACH, LEMONE, SKYBLUE, TOMATO, GREY, GREY, GREY]

pg.init()

class Table():
    pass 


class Ball():
    pass


class Gun():
    def __init__(self, coord=[30, SIZE[1]//2]):
        self.coord = coord
        self.angle = 0
    
    def draw(self,screen):
        end_pos = [self.coord[0] + 30*np.cos(self.angle),
                   self.coord[1] + 30*np.sin(self.angle)]
        pg.draw.lines(screen, SKYBLUE, False, [(self.coord[0], self.coord[1]), 
                                               (self.coord[0], self.coord[1]+10),
                                               (end_pos[0], end_pos[1]+10), 
                                               (end_pos[0], end_pos[1]),
                                               (self.coord[0], self.coord[1])], 2)
        
    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])

    def strike(self):
        pass

class Target():
    pass


class Manager():
    def __init__(self):
        self.gun = Gun()
        self.table = Table()
        
    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        return done
        
    def draw(self, screen):
        screen.fill(BLACK)
        self.gun.draw(screen)
        
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.gun.coord[1] -= 20
                elif event.key == pg.K_DOWN:
                    self.gun.coord[1] += 20
                    
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        return done


screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Why?")
clock = pg.time.Clock()

mgr = Manager()

done = False

while not done:
    clock.tick(15)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
pg.quit()

