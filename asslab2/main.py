import pygame
pygame.init()
import data
if __name__ == "__main__":
  while True:
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
        sys.exit(0)
      if i.type == pygame.KEYDOWN:
        if i.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
          data.currentmenu.back()
        elif i.key in (pygame.K_RETURN, pygame.K_SPACE):
          data.currentmenu.submit()
        elif i.key in (pygame.K_LEFT, pygame.K_a):
          data.currentmenu.left()
        elif i.key in (pygame.K_RIGHT, pygame.K_d):
          data.currentmenu.right()
        elif i.key in (pygame.K_UP, pygame.K_w):
          data.currentmenu.up()
        elif i.key in (pygame.K_DOWN, pygame.K_s):
          data.currentmenu.down()
        else:
          data.currentmenu.text(i.unicode)
    data.currentmenu.run()
    pygame.display.flip()