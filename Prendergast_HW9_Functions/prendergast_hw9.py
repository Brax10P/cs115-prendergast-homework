"""
Braxton Prendergast
3/10/2025
HW9
Frogger
"""


import pygame
from pygame.constants import KEYDOWN
import helper_functions

#init pygame
pygame.init() 

#create font
system_fonts = pygame.font.get_fonts()

my_font = pygame.font.SysFont(system_fonts[0], size = 20, bold=True, italic=False)
hops = 0

#window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width,height))

#set window title
pygame.display.set_caption("Frogger")
direction = "up"

#fps
clock = pygame.time.Clock()
dt = 0
speed = 10

#Setting Frog Current Position
frog_pos = [300,390]



#Car Positions
car1_pos = [0,340]
car2_pos = [575,240]
car3_pos = [0,140]
car4_pos = [520,60]



#Define Cars
frog = pygame.draw.circle(
    screen, 
    "red", 
    frog_pos, 
    10)
car1 = pygame.draw.rect(
    screen, 
    "blue",
    pygame.Rect(car1_pos, (40,40)))
car2 = pygame.draw.circle(
    screen, 
    "purple",
    car2_pos, 25)
car3 = pygame.draw.rect(
    screen, 
    "orange",
    pygame.Rect(car3_pos, (80,40)))
car4 = pygame.draw.ellipse(
        screen,
        "pink",
        pygame.Rect(car4_pos, (80,40)))






""" Game Loop """
running = True
while running:
    """Handle Events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE: #escape key
                running = False
            if event.key == pygame.K_w : #up direction
                frog_pos[1] -= 10 #y-coord
                hops +=1
            if event.key == pygame.K_s : #down
                frog_pos[1] += 10 #y-coord
                hops +=1
            if event.key == pygame.K_a : #left
                frog_pos[0] -= 10 #x-coord
                hops += 1
            if event.key == pygame.K_d : #right
                frog_pos[0] += 10 #x-coord
                hops += 1
    

    """Update Our Game State"""
    #update direction

    if frog_pos[0] < 0:
        frog_pos[0] = 0
        running = False
    if frog_pos[0] > width-10:
        frog_pos[0] = width-10 
        frog_pos = False
    if frog_pos[1] < 0:
        frog_pos[1] = 0
        
    if frog_pos[1] > height-10: 
        frog_pos[1] = height-10
        running = False
        
    

    # Collisions
    if frog_pos == car1_pos:
        running = False
    if frog_pos == car2_pos:
        running = False
    if frog_pos == car3_pos:
        running = False
    if frog_pos == car4_pos:
        running = False

    
    
 
    
        

    
    


    """Draw to our Screen"""
    #clear screen
    screen.fill((128, 128, 128))

    #draw text to screen
    helper_functions.draw_text(f"Hops: {hops}", (0,300), "Green", my_font, screen)
    helper_functions.draw_text(f"Frogger!", (500, 300), "Green", my_font, screen)

    #Win Screen
    if frog_pos[1] == 0:
        helper_functions.draw_text(f"Win!", (275, 200), "Green", my_font, screen)

    #draw safe areas
    pygame.draw.rect(
        screen, 
        "blue", 
        pygame.Rect((0,375), (800,25))
    )

    pygame.draw.rect(
        screen,
        "yellow",
        pygame.Rect((0,175), (800,25))
    )

    pygame.draw.rect(
        screen, 
        "green",
        pygame.Rect((0,0), (800,25))
    )

    #draw lanes
    pygame.draw.rect(
        screen, 
        "white",
        pygame.Rect((0,275), (800,25))
    )

    pygame.draw.rect(
        screen,
        "white",
        pygame.Rect((0,85), (800,25))
    )

    #draw frog
    pygame.draw.circle(
        screen, 
        "red", 
        frog_pos, 
        10)

    #draw cars
    pygame.draw.circle(
        screen, 
        "purple",
        car2_pos, 15)

    pygame.draw.rect(
        screen, 
        "orange",
        pygame.Rect(car3_pos, (20,10))
    )

    pygame.draw.ellipse(
        screen,
        "pink",
        pygame.Rect(car4_pos, (20,10))
    )

    pygame.draw.rect(
        screen, 
        "blue",
        pygame.Rect(car1_pos, (20,20))
    )

    #Setting Car movement
    car1_pos[0] +=30
    car2_pos[0] -=30
    car3_pos[0] +=30
    car4_pos[0] -=30

    if car1_pos[0] >= 600:
        car1_pos[0] = 0
    if car2_pos[0] <= 0:
        car2_pos[0] = 600
    if car3_pos[0] >= 600:
        car3_pos[0] = 0
    if car4_pos[0] <= 0:
        car4_pos[0] = 600
    #update screen
    pygame.display.flip()

    #fps
    dt = clock.tick(speed)/1000

#quit pygame
pygame.quit()

