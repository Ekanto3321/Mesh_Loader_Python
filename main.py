#!/bin/python3

import pygame
import sys
import math 
from math import sin,cos,pi
from object import vertices, faces

pygame.init()

width = 800
height = 800
framerate = 60
size = 1
color = (200,200,50,0.5)
bg = (0,0,0)
dist = 1.75
deg_inc = 0.000005
# window stuff
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D")
clock = pygame.time.Clock()

def main():
    deg = 0.1
    deg_2 = 0
    y_offset = 0
    running = True
    
    paused = False
    vert_to_render = vertices
    faces_to_render = faces

    while running:
        #quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
       
        # refresh 
        screen.fill(bg)
        
        
        # render vertices
        
        # for vertex in vert_to_render:
        #     deg+=deg_inc 
        #     posx,posy,posz = vertex
        #
        #     fin_x, fin_y, fin_z = dostuff(posx,posy,posz,deg)
        #     ren_x, ren_y, ren_z = render(fin_x, fin_y, fin_z)
        #
        #     #pygame.draw.rect(screen, color,(ren_x-size//2,ren_y-size//2, size, size))
        #     #pygame.draw.circle(screen, color, (ren_x, ren_y), size) 
        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            deg -= 0.05
        if keys[pygame.K_RIGHT]:
            deg += 0.05
        if keys[pygame.K_UP]:
            deg_2 -= 0.05
        if keys[pygame.K_DOWN]:
            deg_2 += 0.05
        if keys[pygame.K_s]:
            y_offset -= 0.05
        if keys[pygame.K_w]:
            y_offset += 0.05
        if keys[pygame.K_SPACE]:
            if paused == False: 
                paused = True
            else: 
                paused = False 

        # render faces 
        for i in range(len(faces_to_render)):
            
            if not paused: deg+=deg_inc
            first, second = faces_to_render[i]

            posx,posy,posz = vertices[first]
            posx_2, posy_2, posz_2 = vertices[second]

            fin_x, fin_y, fin_z = dostuff(posx,posy,posz,deg,deg_2,y_offset)
            ren_x, ren_y, ren_z = render(fin_x, fin_y, fin_z)
            
            fin_x2, fin_y2, fin_z2 = dostuff(posx_2,posy_2,posz_2,deg,deg_2, y_offset)
            ren_x2, ren_y2, ren_z2 = render(fin_x2, fin_y2, fin_z2)

            pygame.draw.line(screen, color, (ren_x, ren_y), (ren_x2, ren_y2), 1)

            

        pygame.display.flip()
        clock.tick(framerate)
    pygame.quit()
    sys.exit()


# vertices
#vertices = [
#    (-1, 1,-1), 
#    ( 1, 1,-1), 
#    ( 1,-1,-1), 
#    (-1,-1,-1), 
#    (-1, 1, 1),  
#    ( 1, 1, 1),  
#    ( 1,-1, 1),  
#    (-1,-1, 1)    
#]

# edge connections 
#faces = [
#    (0,1), (1,2), (2,3), (3,0),
#    (4,5), (5,6), (6,7), (7,4),
#    (0,4), (1,5), (2,6), (3,7)
#]



def dostuff(x,y,z, deg, deg_2, y_offset):

    # #along y axis
    # fin_x = x*math.cos(deg) - z*math.sin(deg)
    # fin_z = dist + x*math.sin(deg) + z*math.cos(deg) 
    # fin_y = y
 
    #along x axis 
    fin_x = x 
    fin_z = y * math.sin(deg_2) + z * math.cos(deg_2)
    fin_y = y * math.cos(deg_2) - z * math.sin(deg_2)
    
     #along y axis
    fin2_x = fin_x*math.cos(deg) - fin_z*math.sin(deg)
    fin2_z = dist + fin_x*math.sin(deg) + fin_z*math.cos(deg) 
    fin2_y = fin_y
 

    
    fin3_x = fin2_x 
    fin3_y = fin2_y + y_offset
    fin3_z = fin2_z


    return (fin3_x, fin3_y, fin3_z)



def render(x, y, z):
    
    x = x/z
    y = y/z
    fixed_z = (((z+1))/2*width)
    fixed_x = (((x+1))/2*height)
    fixed_y = height-(((y+1))/2*width)
    return (int(fixed_x), int(fixed_y), int(fixed_z))

if __name__ == "__main__":
    main()

