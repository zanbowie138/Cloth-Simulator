import pygame;
import math;
import random

from pygame.locals import *
import utils
from cloth import Cloth

def update_fps():
	fps = f"FPS: {str(int(clock.get_fps()))}"
	return text_render(fps)

def text_render(string):
    return font.render(string, 1, pygame.Color("white"))
 
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)
 
gameOn = True
update_count = 0

cloth = Cloth(300,300,50,30,5)
cloth.generate_points()

while gameOn:
    clock.tick(60)
    update_count+=1

    #keys = pygame.key.get_pressed()
    #if pygame.mouse.get_pressed():
    #    pass

    #Create background
    screen.fill((0,0,0))

    #Update fps
    screen.blit(update_fps(), (10,0))
    screen.blit(text_render(f"Frame #: {update_count}"), (10,30))
 
    for stick in cloth.sticks:
        pygame.draw.line(screen, (120,120,255), (stick.p1.x, stick.p1.y), (stick.p2.x, stick.p2.y))

    # Update the display using flip
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
            pygame.quit()
            continue

pygame.quit()