#------ 
#Helper Functions
#-----
"""This Function Draws Text to Screen
Text: What to say
Coordinate: Coord Values
text_color: Color of Text
"""

def draw_text(text, coordinate, text_color, my_font, screen):
  text_image = my_font.render(text, True, text_color)
  text_rect = text_image.get_rect()
  text_rect.topleft = coordinate
  screen.blit(text_image, text_rect)