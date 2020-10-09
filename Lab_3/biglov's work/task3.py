#!/usr/bin/env python3

# Task 9_1 chosen by RNG
import pygame
import numpy as np
import pygame.draw as dr
import pygame.transform as trans


COLORS = {"grey": (230, 230, 230),
          "dark-grey": (50, 50, 50),
          "water": (22, 80, 68),
          "black": (0, 0, 0),
          "sky": (0, 255, 255)}


def bordered_ellipse(screen, color, rect, width):
    dr.ellipse(screen, color, rect)
    dr.ellipse(screen, COLORS["black"], rect, width)


def draw_background(screen):
    width, height = screen.get_width(), screen.get_height()
    screen.fill(COLORS["sky"])
    dr.rect(screen, COLORS["grey"], [0, height//2, width, height//2])
    dr.line(screen, COLORS["black"], (0, height//2), (width, height//2))


def draw_poodle(screen, x, y, scale):
    w, h = 100*scale, 50*scale
    rect1 = [x - w//2, y - h//2, w, h]
    bordered_ellipse(screen, COLORS["dark-grey"], rect1, 2)
    w2, h2 = 3*w//4, 3*h//4
    rect2 = [x - w2//2, y + h//2 - h2, w2, h2]
    bordered_ellipse(screen, COLORS["water"], rect2, 2)


def draw_bear_head(screen, x, y, scale):
    w, h = 100*scale, 60*scale
    rect = [int(c) for c in [x - w//2, y - h//2, w, h]]
    
    # base
    bordered_ellipse(screen, COLORS["grey"], rect, 2)

    # eye and nose
    dr.ellipse(screen, COLORS["black"], [x - w//6, y - h//5, w//8, h//8])
    dr.ellipse(screen, COLORS["black"], [x + 4*w//9, y - h//7, w//8, h//8])

    # mouth
    m_w, m_h = int(w*1.1), h//4
    dx, dy = int(-7*scale), int(3*scale)
    mouth_rect = [x - m_w//2 + dx, y - m_h//2 + dy, m_w, m_h]
    dr.arc(screen, COLORS["black"], mouth_rect, 3*np.pi/2, 2*np.pi)

    # ear
    e_x, e_y = x - 3*w//9, y - 3*h//9
    e_w, e_h = w//5, h//5

    ear_rect1 = [e_x - e_w//2, e_y - e_h//2, e_w, e_h]
    ear_rect2 = [e_x - e_w//2, e_y - e_h, e_w, e_h*2]
    dr.ellipse(screen, COLORS["grey"], ear_rect1)
    dr.arc(screen, COLORS["black"], ear_rect1, 0, 1.1*np.pi, 2)
    dr.arc(screen, COLORS["black"], ear_rect2, 1.05*np.pi, 2*np.pi, 2)

def draw_pole(screen, x, y, scale):
    segment_len = int(60*scale)
    segment_ang = [-np.pi/3, -np.pi/4, -np.pi/4 - 0.05, -np.pi/4 + 0.05, -np.pi/4]
    width = 6*scale

    x_c, y_c = x, y
    for ang in segment_ang:
        dx, dy = int(segment_len*np.cos(ang)), int(segment_len*np.sin(ang))
        dr.line(screen, COLORS["black"], (x_c, y_c), (x_c+dx, y_c+dy), width)
        x_c += dx
        y_c += dy
    ye = y + segment_len
    dr.line(screen, COLORS["black"], (x_c, y_c), (x_c, ye))
    

def draw_bear(screen, x, y, scale):
    w, h = int(180*scale), int(300*scale)   
    draw_bear_head(screen, x + w//4, y -6*h//11, scale)

    #body
    bordered_ellipse(screen, COLORS["grey"], [x - w//2, y - h//2, w, h], 2)

    #legs
    bordered_ellipse(screen, COLORS["grey"], [x, y + h//4, w//2, h//4], 2)
    bordered_ellipse(screen, COLORS["grey"], [x + w//4, y + 3*h//7, w//2, h//10], 2)

    #fishing pole
    draw_pole(screen, x + 6*w//10, y - h//14, scale)

    #arms
    bordered_ellipse(screen, COLORS["grey"], [x + w//3, y - h//4, w//2, h//16], 2)


def draw_fish(screen, x, y, ang, scale):
    srf = FISH_IMG.copy()    
    srf = trans.rotate(srf, ang)
    srf = trans.scale(srf, (int(srf.get_width()*scale), int(srf.get_height()*scale)))
    screen.blit(srf, (x, y))


def draw_scene(screen, x, y, scale):
    draw_poodle(screen, x + 125*scale, y + 40*scale, 1.5*scale)
    draw_bear(screen, x - 180*scale, y, scale)
    draw_fish(screen, x + 40*scale, y + 45*scale, 10, scale/2)


pygame.init()
FISH_IMG = pygame.image.load("fish.png")

pygame.display.set_caption("the video clip of FISH&BEAR")
done = False
clock = pygame.time.Clock()

pygame.mixer.music.load('fendi.mp3')
pygame.mixer.music.play()

imageImg=[pygame.image.load('fish-min.png')]*3
k=0
imagex = [100,50,300]
imagey = [200,150,100]
direction =['left','right','down']

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    k+=5

    screen = pygame.display.set_mode((600, 900))
    draw_background(screen)
    scene_srf = pygame.Surface((600, 900))
    scene_srf.set_colorkey((0, 255, 0))
    scene_srf.fill((0, 255, 0))
    draw_scene(scene_srf, scene_srf.get_width()//2, scene_srf.get_height()//2, 1)
    screen.blit(scene_srf, (0,0))
    pygame.display.update()
    clock = pygame.time.Clock()
    
    for i in range(3):
        if direction[i] == 'right':
            imagex[i] += 5
            if imagex[i] == 40:
                direction[i] = 'down'
        elif direction[i] == 'down':
            imagey[i] += 5
            if imagey[i] == 40:
                direction[i] = 'left'
        elif direction[i] == 'left':
            imagex[i] -= 5
            if imagex[i] == 20:
                direction[i] = 'up'
        elif direction[i] == 'up':
            imagey[i] -= 5
            if imagey[i] == 20:
                direction[i] = 'right'
        screen.blit(imageImg[i], (imagex[i]/1.5, imagey[i]/1.5))
    screen.blit(FISH_IMG,(200+k,200))  
    screen.blit(FISH_IMG,(200+5*k/5,200)) 
    
    f2 = pygame.font.SysFont('serif', 28)
    text2 = f2.render("Это всё, до чего я додумалась", 0, (0, 180, 0))
    screen.blit(text2, (180, 20))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()