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

pg.init()

class Table():
    pass 


class Ball():
    pass


class Gun():
    pass
    '''def __init__(self, coord=[30, SIZE[1]//2]):
        self.coord = coord
        self.angle = 0
    
    def draw(self,screen):
        pass
    def strike(self):
        pass'''

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
        # self.gun.draw(draw)
        
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
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