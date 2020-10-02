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







#объект содерж экран
screen=pygame.display.set_mode([640,480])
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
    screen.fill(LSALMON)
    pygame.draw.rect(screen,PEACH,(0, 96, 640, 96))
    pygame.draw.rect(screen,LEMONE,(0, 192, 640, 96))
    pygame.draw.rect(screen,SKYBLUE,(0, 288, 640, 192))

    #be like a sun, be happy!
    pygame.draw.circle(screen,TOMATO,[320,96],40)
    
    
    #we can see mountains far away.
    pygame.draw.polygon(screen,CADET,[(640,144),(586,120),(510,160)])
    pygame.draw.polygon(screen,CADET,[(580,150),(510,110),(453,166)])
    pygame.draw.ellipse(screen,CADET,(503,107,30,30))
    pygame.draw.ellipse(screen,CADET,(525,124,30,30))
    pygame.draw.polygon(screen,CADET,[(527,111),(551,130),(510,160)])
    pygame.draw.polygon(screen,CADET,[(400,171),(480,86),(510,160)])
    pygame.draw.polygon(screen,CADET,[(400,171),(300,182),(346,153)])
    pygame.draw.polygon(screen,CADET,[(510,160),(330,176),(386,143)])
    pygame.draw.rect(screen,CADET,(386,130,60,20))
    pygame.draw.ellipse(screen,PEACH,(370,110,60,40))
    pygame.draw.ellipse(screen,CADET,(462,85,29,50))
    pygame.draw.polygon(screen,CADET,[(430,135),(465,94),(480,110)])
    pygame.draw.polygon(screen,PEACH,[(428,137),(465,94),(410,135)])
    pygame.draw.polygon(screen,CADET,[(133,92),(160,105),(160,160)])
    pygame.draw.polygon(screen,CADET,[(300,182),(100,205),(280,170)])
    pygame.draw.polygon(screen,CADET,[(300,182),(40,177),(0,217)])  
    pygame.draw.polygon(screen,CADET,[(250,188),(130,90),(64,210)]) 
    pygame.draw.rect(screen,CADET,(40,150,60,50))
    pygame.draw.ellipse(screen,PEACH,(20,130,70,50))
    pygame.draw.polygon(screen,PEACH,[(89,160),(70,155),(126,96)])
    
    
    #Mountains in the middle
    pygame.draw.ellipse(screen,SLATE,(5,190,90,208))
    pygame.draw.polygon(screen,SLATE,[(80,288),(250,288),(160,250)]) 
    pygame.draw.polygon(screen,SLATE,[(190,288),(300,288),(260,210)])
    pygame.draw.polygon(screen,SLATE,[(190,288),(210,200),(260,210)])
    pygame.draw.polygon(screen,SLATE,[(190,288),(440,288),(380,230)])
    pygame.draw.polygon(screen,SLATE,[(440,288),(570,205),(640,288)])
    pygame.draw.polygon(screen,SLATE,[(600,288),(640,288),(640,160)])
    pygame.draw.polygon(screen,SLATE,[(600,288),(615,210),(640,203)])
    pygame.draw.ellipse(screen,SLATE,(340,210,80,70))
    pygame.draw.ellipse(screen,SLATE,(354,210,70,40))
    pygame.draw.polygon(screen,SLATE,[(400,288),(640,288),(410,220)])
    pygame.draw.ellipse(screen,LEMONE,(433,215,80,40))
    pygame.draw.polygon(screen,LEMONE,[(433,238),(402,205),(450,220)])
    pygame.draw.polygon(screen,SLATE,[(317,268),(344,230),(370,280)])


    #mountains are in front of us.
    pygame.draw.polygon(screen,DARK,[(0,480),(0,250),(60,263)])
    pygame.draw.polygon(screen,DARK,[(0,480),(155,340),(60,263)])
    pygame.draw.polygon(screen,DARK,[(0,480),(155,340),(230,480)])
    pygame.draw.polygon(screen,DARK,[(270,480),(440,400),(500,480)])
    pygame.draw.rect(screen,DARK,(210,460,60,20))
    pygame.draw.ellipse(screen,SKYBLUE,(221,441,80,38))
    pygame.draw.polygon(screen,DARK,[(0,480),(155,340),(230,480)])
    pygame.draw.ellipse(screen,DARK,(540,280,200,400))
    pygame.draw.rect(screen,DARK,(470,400,80,108))
    pygame.draw.ellipse(screen,SKYBLUE,(221,441,80,38))
    pygame.draw.ellipse(screen,SKYBLUE,(459,347,89,110))
    
    
    #I HATE this STUff. Birds
    pygame.draw.arc(screen, BROWN, (300, 280, 60, 40),0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (300+50, 280-2, 60, 30),1.6, 3,5)
    pygame.draw.lines(screen,BROWN,False,[[300+23,280+3],
                                          [300+52,280+12],
                                          [300+78,280-1]],6)
    pygame.draw.arc(screen, BROWN, (430, 360, 60, 40),0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (430+50, 360-2, 60, 30),1.6, 3,5)
    pygame.draw.lines(screen,BROWN,False,[[430+23,360+3],
                                          [430+52,360+12],
                                          [430+78,360-1]],6)
    
    pygame.draw.arc(screen, BROWN, (350, 330, 0.7*60, 0.7*40),0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (350+0.7*50, 330-1.4, 0.7*60, 0.7*30),1.6, 3,5)
    pygame.draw.lines(screen,BROWN,False,[[350+0.7*23,330+2.1],
                                          [350+0.7*52,330+0.7*12],
                                          [350+0.7*78,330-0.7]],6)
    pygame.draw.arc(screen, BROWN, (400, 315, 0.7*60, 0.7*40),0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (400+0.7*50, 315-1.4, 0.7*60, 0.7*30),1.6, 3,5)
    pygame.draw.lines(screen,BROWN,False,[[400+0.7*23,315+2.1],
                                          [400+0.7*52,315+0.7*12],
                                          [400+0.7*78,315-0.7]],6)
    pygame.draw.arc(screen, BROWN, (320, 160, 0.5*60, 0.5*40),0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (320+0.5*50, 160-1, 0.5*60, 0.5*30),1.6, 3,5)
    pygame.draw.lines(screen,BROWN,False,[[320+0.5*23,160+1.5],
                                          [320+0.5*52,160+0.5*12],
                                          [320+0.5*78,160-0.5]],4)
    pygame.draw.arc(screen, BROWN, (290, 140, 0.5*60, 0.5*40),0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (290+0.5*50, 140-1, 0.5*60, 0.5*30),1.6, 3,5)
    pygame.draw.lines(screen,BROWN,False,[[290+0.5*23,140+1.5],
                                          [290+0.5*52,140+0.5*12],
                                          [290+0.5*78,140-0.5]],4)
    pygame.draw.arc(screen, BROWN, (270, 170, 0.5*60, 0.5*40),0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (270+0.5*50, 170-1, 0.5*60, 0.5*30),1.6, 3,5)
    pygame.draw.lines(screen,BROWN,False,[[270+0.5*23,170+1.5],
                                          [270+0.5*52,170+0.5*12],
                                          [270+0.5*78,170-0.5]],4)   
    pygame.draw.arc(screen, BROWN, (260, 220, 0.5*60, 0.5*40),0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (260+0.5*50, 220-1, 0.5*60, 0.5*30),1.6, 3,5)
    pygame.draw.lines(screen,BROWN,False,[[260+0.5*23,220+1.5],
                                          [260+0.5*52,220+0.5*12],
                                          [260+0.5*78,220-0.5]],4)
    
    
    
    
    
    
    pygame.display.flip()
pygame.quit()


'''    #нарисуем линию 5-толщина
    pygame.draw.line(screen,BLUE,[100,50],[100,150],5)
    pygame.draw.line(screen,BLUE,[400,50],[400,150],5)
    pygame.draw.lines(screen,BLUE,False,[[270,150],[270,50],[320,50],[320,150]],5)
    pygame.draw.ellipse(screen,BLUE,[50,70,100,60],5)

    pygame.draw.ellipse(screen,BLUE,[350,70,100,60],5)
    pygame.draw.ellipse(screen,BLUE,[170,50,70,100],5)
'''