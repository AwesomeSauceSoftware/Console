import menus
import pygame
import asscore
class Background:
  def blit(self):
    display.fill((0,0,255))
    nametext = font.render(username, False, (0, 255, 255))
    display.blit(nametext, (display.get_width()-nametext.get_width()-10, 10))
    systemtext = font.render(asscore.systemname, False, (0,255,255))
    display.blit(systemtext, (10, 10))
display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
background = Background()
currentmenu = menus.mainMenu
font = pygame.font.SysFont("Papyrus Bold", 30)
username = "Not Logged In."
password = ""
sid = "0000000000"