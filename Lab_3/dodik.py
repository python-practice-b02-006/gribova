# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:17:17 2020

@author: Nika
"""

import pygame
BLACK=(0,0,0)
BLUE=(0,0,255)
LSALMON=(255,160,122)
PEACH=(255, 218, 185)
LEMONE=(255, 250, 205)
SKYBLUE=(100, 149, 237)
TOMATO=(255, 99, 71)
CADET=(176, 196, 222)
SLATE=(106, 90, 205)
DARK=(72, 61, 109)
BROWN=(139, 69, 19)
pygame.init()







screen=pygame.display.set_mode([500,500])
pygame.display.set_caption('My first pygame app window caption')
done=False
#задержка
clock=pygame.time.Clock()


while not done:
    clock.tick(10)

    for event in pygame.event.get():
        #все нажатия после гэт
        if event.type==pygame.QUIT:
            done=True

    #The colours of background
    screen.fill((128, 128, 128))
    pygame.draw.circle(screen,(255, 255, 0),(250,250),200)
    pygame.draw.arc(screen, BLACK, (50, 50, 400, 400),0, 7)
    pygame.draw.line(screen, BLACK, (150,350),(350,350),40)
    pygame.draw.circle(screen,(128, 0, 0),(180,180),40)
    pygame.draw.arc(screen, BLACK, (140, 140, 80, 80), 0, 7, 4)
    pygame.draw.circle(screen,BLACK,(180,180),10)
    pygame.draw.circle(screen,(128, 0, 0),(320,180),30)
    pygame.draw.arc(screen, BLACK, (290, 150, 60, 60), 0, 7, 4)
    pygame.draw.circle(screen,BLACK,(320,180),10)
    pygame.draw.polygon(screen,BLACK,[(70,65),(230,165),(236,155),(76,55)])
    pygame.draw.polygon(screen,BLACK,[(430,85),(436,95),(270,175),(264,165)])

    pygame.display.flip()
pygame.quit()