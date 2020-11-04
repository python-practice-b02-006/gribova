# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:34:28 2020

@author: Nika
"""
import numpy as np
import pygame as pg
from random import randint

SIZE = (728, 410)

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


class Table():
    def __init__(self, t_destr=0, b_used=0):
        self.t_destr = t_destr
        self.b_used = b_used
        self.font = pg.font.SysFont("dejavusansmono", 25)

    def score(self):
        return self.t_destr - self.b_used
    
    def draw(self, screen):
        score_surf = []
        score_surf.append(self.font.render("Destroyed: {}".format(self.t_destr), True, TOMATO))
        score_surf.append(self.font.render("Balls used: {}".format(self.b_used), True, PEACH))
        score_surf.append(self.font.render("Total: {}".format(self.score()), True, PEACH))
        for i in range(3):
            screen.blit(score_surf[i], [10, 10 + 30*i])

class Ball():
    def __init__(self, coord, vel, rad=15, color=None):
        if color == None:
            color = COLORS[randint(0,len(COLORS)-1)]
        self.alive=True
        self.color = color
        self.coord = coord
        self.vel = vel
        self.rad = rad

    def move(self, t_step=1, g=3):
        self.vel[1] += int(g * t_step)
        for i in range(2):
            self.coord[i] += int(self.vel[i] * t_step)
        self.wall()
        if self.vel[0]**2 + self.vel[1]**2 < 2**2 and self.coord[1] > SIZE[1] - 2*self.rad:
               self.is_alive = False

    def wall(self):
        n = [[1, 0], [0, 1]]
        obstacles = [[[410, 400], [430,380]], [[510, 210],[530, 190]], 
             [[610, 20], [630, 0]], [[640, 90], [660, 70]], [[530, 310], [550,290]]]
        for i in range(2):
            if self.coord[i] < self.rad:
                self.coord[i] = self.rad
                self.flip_vel(n[i])
            elif self.coord[i] > SIZE[i] - self.rad:
                self.coord[i] = SIZE[i] - self.rad
                self.flip_vel(n[i])
        for i in range(5):
            for j in range(2):
                if (self.coord[0] - obstacles[i][j][0])**2 + (self.coord[1] - obstacles[i][j][1])**2 < self.rad**2:                 
                    if self.vel[0]>0:
                        self.coord[0] = int(obstacles[i][j][0]-self.rad/2**0.5)
                    else:self.coord[0] = int(obstacles[i][j][0]+self.rad/2**0.5)
                    if self.vel[1]>0:
                        self.coord[1] = int(obstacles[i][j][1] -self.rad/2**0.5)
                    else:self.coord[1] = int(obstacles[i][j][1] +self.rad/2**0.5)
                    self.flip_vel(n[0])
                    self.flip_vel(n[1])
    


    def flip_vel(self, axis, coef_perp=1, coef_par=1):
        vel = np.array(self.vel)
        n = np.array(axis)
        n = n / np.linalg.norm(n)
        vel_perp = vel.dot(n) * n #скалярное произведение массиввов
        vel_par = vel - vel_perp
        ans = -0.9*vel_perp * coef_perp + 0.93*vel_par * coef_par
        self.vel = ans.astype(np.int).tolist()    
    
    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)


class Gun():
    def __init__(self, coord=[30, SIZE[1]//2], minp=30, maxp=40):
        self.coord = coord
        self.angle = 0
        self.min_pow = minp
        self.max_pow = maxp
        self.power = minp
        self.active = False
    
    def draw(self, screen):
        end_pos = [self.coord[0] + 30*np.cos(self.angle),
                   self.coord[1] + 30*np.sin(self.angle)]
        pg.draw.lines(screen, PEACH, False, [(self.coord[0], self.coord[1]), 
                                               (self.coord[0], self.coord[1]+10),
                                               (end_pos[0], end_pos[1]+10), 
                                               (end_pos[0], end_pos[1]),
                                               (self.coord[0], self.coord[1])], 6)
        
    def move(self):
        if self.active and self.power < self.max_pow:
            self.power+=1
    
    def set_angle(self, mouse_pos):
        self.angle = np.arctan2(mouse_pos[1] - self.coord[1], 
                                mouse_pos[0] - self.coord[0])

    def spit(self):
        vel = [int(self.power * np.cos(self.angle)), 
               int(self.power * np.sin(self.angle))]
        return Ball(list(self.coord), vel)

class Target():
    def __init__(self, coord=None, color=None, r=30):
        if coord == None:
            coord = [randint(r, SIZE[0] - r), randint(r, SIZE[1] - r)]
        self.coord = coord
        self.rad = r
        if color == None:
            color = COLORS[randint(0,len(COLORS)-1)]
        self.color = color

    def draw(self, screen):
        pg.draw.circle(screen, self.color, self.coord, self.rad)
        

class Manager():
    def __init__(self, n_targets):
        self.gun = Gun()
        self.score_t = Table()
        self.targets = []
        self.n_targets = n_targets
        self.balls = []   
        self.missions()
        
    
    
        
    def move(self):
        self.gun.move()
        for i in self.balls:
            i.move()
        
    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        self.move()
        self.check_alive()
        if len(self.targets) == 0 and len(self.balls) == 0:
            self.missions()
        return done
        
    def draw(self, screen):
        screen.blit(SC_IMG, (0, 0))
        self.gun.draw(screen)
        for i in self.balls:
            i.draw(screen)
        obstacles = [[(410, 400), (430,380)], [(510, 210),(530, 190)], 
             [(610, 20), (630, 0)], [(640, 90), (660, 70)], [(530, 310), (550,290)]]
        for i in range(5):
            pg.draw.line(screen, TOMATO, obstacles[i][0], obstacles[i][1], 15)
        for target in self.targets:
            target.draw(screen)
        
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
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gun.active = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.balls.append(self.gun.spit())
                    self.score_t.b_used += 1
                    
        if pg.mouse.get_focused():
            mouse_pos = pg.mouse.get_pos()
            self.gun.set_angle(mouse_pos)
        return done
    
    def check_alive(self):
        dead_balls = []
        for i, ball in enumerate(self.balls):
            if not ball.alive:
                dead_balls.append(i)

        for i in reversed(dead_balls):
            self.balls.pop(i)
    def missions(self):
        for i in range(self.n_targets):
            self.targets.append(Target(r=randint(max(1, 30 - 2*max(0, self.score_t.score())), 
                30 - max(0, self.score_t.score()))))

screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Nikita's work")
clock = pg.time.Clock()

mgr = Manager(3)

done = False

SC_IMG = pg.image.load("night.jpg")
screen.blit(SC_IMG, (0, 0))

while not done:
    clock.tick(15)
    done = mgr.process(pg.event.get(), screen)
    pg.display.flip()
    
    
pg.quit()

