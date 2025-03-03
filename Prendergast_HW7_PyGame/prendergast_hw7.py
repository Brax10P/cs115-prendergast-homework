import pygame

#init pygame
pygame.init() 

#window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width,height))

#set window title
pygame.display.set_caption("Frogger")

#fps
clock = pygame.time.Clock()
dt = 0
speed = 10

""" Game Loop """
running = True
while running:
  """Handle Events"""
  for event in pygame.event.get():
    if event.type == pygame.quit:
      running = False


  """Update Our Game State"""


  """Draw to our Screen"""
  #clear screen
  screen.fill((128, 128, 128))

  #draw rectangle
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

  #Draw Circle
  pygame.draw.circle(
    screen, 
    "green", 
    (100,200), 
    40)

  #Draw a Line
  pygame.draw.line(
    screen, 
    "red", 
    (100,100), 
    (200,200), 
    5)


  #update screen
  pygame.display.flip()

  #fps
  dt = clock.tick(speed)/1000

#quit pygame
pygame.quit()

