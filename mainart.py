import pygame
from pygame.draw import *
from random import *

def tree(x,y,size):
     ellipse(screen,(34,139,34),[(x,y),(size*70,size*60)])
     ellipse(screen,(0,255,0),[(x,y),(size*70,size*60)], size*2)
     ellipse(screen,(255,222,173),[(x+size*45,y+size*25),(size*18,size*14)])
     ellipse(screen,(0,255,0),[(x+size*45,y+size*25),(size*18,size*14)],size*2)
     ellipse(screen,(34,139,34),[(x-size*25,y+size*40),(size*120,size*70)])
     ellipse(screen,(0,255,0),[(x-size*25,y+size*40),(size*120,size*70)],size*2)
     ellipse(screen,(255,222,173),[(x+size*60,y+size*70),(size*18,size*14)])
     ellipse(screen,(0,255,0),[(x+size*60,y+size*70),(size*18,size*14)],size*2)
     ellipse(screen,(34,139,34),[(x,y+size*90),(size*70,size*60)])
     ellipse(screen,(0,255,0),[(x,y+size*90),(size*70,size*60)],size*2)
     ellipse(screen,(255,222,173),[(x+size*45,y+size*113),(size*18,size*14)])
     ellipse(screen,(0,255,0),[(x+size*45,y+size*113),(size*18,size*14)],size*2)
     polygon(screen,(139,69,19), [(x+size*32,y+size*150), (x+size*38,y+size*150),
                                  (x+size*38,y+size*190),(x+size*32,y+size*190)])

def griva(dir,size,x,y,k,l):
    for i in range(5):
        ellipse(screen, (255-13*i,160+i*15,122), [(x-dir*size*((i+2)*9+36-k)+size*36, y + size*((i+1)*15-l)), (size*25,size*15)])
        ellipse(screen, (255-12*i,110+15*i,80), [(x-dir*size*(i*4+15+38-k)+size*38, y + size*((i+1)*16-l)), (size*20,size*17)])
        ellipse(screen, (173,255-15*i,47+10*i), [(x-dir*size*(i*4+40-k)+size*40, y + size*(((i+1)*14)-l)), (size*18,size*14)])
        ellipse(screen, (148,0+15*i,211), [(x-dir*size*(i*2+43-k)+size*43, y + size*(((i+1)*15)-l)), (size*14,size*10)])
        ellipse(screen, (106,90+15*i,205), [(x-dir*size*(20+i*5+42-k)+size*42, y + size*(((i+2)*14)-l)), (size*12,size*10)])

def unicorn(dir,x,y,size):
#draw main body
    ellipse(screen, (255,255,255), [(x,y),(size*100,size*53)])
#draw legs
    polygon(screen, (255,255,255), [(x+size*50+dir*size*25, y+size*45), (x+size*50+dir*size*32,  y+size*45),
           (x+size*50+dir*size*32,  y+size*100), (x+size*50+dir*size*25, y+size*100)])
    polygon(screen, (255,255,255), [(x+size*50+dir*size*40, y+size*30), (x+size*50+dir*size*47,  y+size*30),
           (x+size*50+dir*size*47,  y+size*90), (x+size*50+dir*size*40, y+size*90)])
    polygon(screen, (255,255,255), [(x+size*50-dir*size*25, y+size*45), (x+size*50-dir*size*32,  y+size*45),
           (x+size*50-dir*size*32,  y+size*90), (x+size*50-dir*size*25, y+size*90)])
    polygon(screen, (255,255,255), [(x+size*50-dir*size*40, y+size*30), (x+size*50-dir*size*47,  y+size*30),
           (x+size*50-dir*size*47,  y+size*105), (x+size*50-dir*size*40, y+size*105)])
#draw face
    polygon(screen, (255,255,255), [(x+size*50+dir*size*30, y+size*30), (x+size*50+dir*size*48,  y+size*30),
           (x+size*50+dir*size*48,  y-size*50), (x+size*50+dir*size*30, y-size*50)])
    ellipse(screen, (255,255,255), [(x+size*50+dir*size*51-size*26,y-size*75), (size*52,size*37)])
    ellipse(screen, (255,255,255), [(x+size*50+dir*size*75-size*15,y-size*64), (size*30,size*18)])
    polygon(screen, (251,0,51), [(x+size*50+dir*size*50,y-size*74),(x+size*50+dir*size*58,y-size*74),
                                 (x+size*50+dir*size*56,y-size*110)])
#draw eyes 
    circle(screen, (255,105,180), (x+size*50+dir*size*58, y-size*60), size*6)
    circle(screen, (0,0,44), (x+size*50+dir*size*60, y-size*59), size*4)
    circle(screen, (255,255,255), (x+size*50+dir*size*57, y-size*62),size*2)
#draw mane, k and l - position of mane. (0,0) - tail  
    griva(dir,size,x,y,80,90)
    griva(dir,size,x,y,0,0)
    
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
#draw painting background 
polygon(screen, (135,206,235),[(0,0),(0,350),(600,350),(600,0)])
polygon(screen, (0,255,127),[(0,350),(0,800),(600,800),(800,350)])
circle(screen,(255,215,0,255),(460,200),50)
circle(screen,(255,215,0,0),(460,200),30)
#draw main characters 
tree(0,0,2)
tree(100,50,2)
tree(0,100,2)
tree(75,400,1)
tree(25,450,1)
unicorn(1,400,300,1)
unicorn(-1,200,450,1)
unicorn(1,250,600,2)
unicorn(-1,550,400,1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()