# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:40:35 2020

@author: Nika
"""
'''
import pygame as pg
import random

FPS=10
clock=pg.time.Clock()
screen = pg.display.set_mode((640,480))
done = False

pg.font.init()
font_1 = pg.font.SysFont('Times New Roman', 28)
    

#ball_coords=list([random.rand()]*4)
class Balls():
    def _init_(self, n_balls):
        self.balls = list([[random.randn(0,639), random.randn(0,479)] for i in range(n_balls)])
        
        
while not done:
    clock.tick(10)
    x, y = (0, 0)
    for event in pg.event.get():
        if event == pg.QUIT:
            done = True
        elif event == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
    text_surf = font_1.render("{},{}".format(x,y),False,(255,0,0))'''
import pygame
from random import randint
sc = 0

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


class Balls():
    def __init__(self, n_balls):
        self.n = n_balls
        self.colors = list([COLORS[randint(0, len(COLORS)-1)] for i in range(n_balls)])
        self.radius = list([randint(10, 70) for i in range(n_balls)])
        self.areas = list([[randint(0,1019-self.radius[i]), randint(0,639--self.radius[i])] for i in range(n_balls)])
        self.speed = list([[randint(-5, 5), randint(-5,5)] for i in range(n_balls)])
        
        self.score = 0
    
    
    def draw_all_balls(self, screen):
        for i in range(self.n):
            pygame.draw.circle(screen, self.colors[i], 
                               self.areas[i], self.radius[i])


    def tyk(self, x, y):
        global sc
        for i in range(self.n):
            if (int(self.areas[i][0]) - int(x))**2 + (int(self.areas[i][1]) - int(y))**2 < self.radius[i]**2:                
                if self.colors[i] == GREY: 
                    self.score += 100                  
                else:
                    self.score += (1000/self.radius[i])//3
                sc = self.score
                self.radius[i] = randint(10, 70)
                self.areas[i] = [randint(0,1019-self.radius[i]), randint(0,639--self.radius[i])]
                self.speed[i] = [randint(-self.speed[i][0]-5, self.speed[i][1]+5), 
                                 randint(-self.speed[i][0]-5, self.speed[i][1]+5)]
                return (True,sc)


    def iterate(self, tick):
        for i, ball in enumerate(self.areas):
            for k in range(2):
                self.areas[i][k] += self.speed[i][k] * tick
            if ball[0] > 1019-self.radius[i]:
                self.areas[i][0] = 1019-self.radius[i]
                self.speed[i][0] *= -1
            elif ball[0] < self.radius[i]:
                self.areas[i][0] = self.radius[i]
                self.speed[i][0] *= -1
            elif ball[1] > 639-self.radius[i]:
                self.areas[i][1] = 639-self.radius[i]
                self.speed[i][1] *= -1
            elif ball[1] < self.radius[i]:
                self.areas[i][1] = self.radius[i]
                self.speed[i][1] *= -1    

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

FPS = 5
screen = pygame.display.set_mode((1020, 640))

k = 0
x = 0
y = 0
finished = False

balls = Balls(20)

font_1 = pygame.font.SysFont("serif", 40)
font_2 = pygame.font.SysFont("serif", 30)
font_3 = pygame.font.SysFont("Times New Roman", 20)

hooray_IMG = pygame.image.load("hooray.jpg")
loser_IMG = pygame.image.load('loser.jpg')

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:           
            x = event.pos[0]
            y = event.pos[1]
            k += 1
    screen.fill((125,125,125))
    balls.tyk(x, y)
    balls.iterate(1)
    balls.draw_all_balls(screen)
    score_surf1 = font_1.render("Score: {}".format(balls.score), False, (255, 0, 0))
    score_surf2 = font_2.render("if you want to quit, push 'esc' then quit", False, (255, 0, 0))
    screen.blit(score_surf1, (10, 30))
    screen.blit(score_surf2, (100, 550))   
    pygame.display.update()
finished = False
while not finished:
    screen.fill(PEACH)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        
    if sc >= k*100:
        screen.blit(hooray_IMG,(50,100)) 
    else: 
        screen.blit(loser_IMG,(50,100)) 
        score_surf3 = font_3.render("Ты что ещё не догадался на какой цвет нажимать?!? ", False, DARK)
        screen.blit(score_surf3, (10, 30))
    score_surf4 = font_3.render("Максимальный результат {}, твой результат {}".format(100*k,sc), False, TOMATO)
    screen.blit(score_surf4, (10, 50))

    pygame.display.update()
    
    #screen.blit(hooray_IMG,(200,200))    
pygame.quit()
    