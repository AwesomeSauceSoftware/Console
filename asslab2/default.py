import pygame
import sys
import os
import data
import menus
class MenuProxy:
  def __init__(self, menu):
    self.menu = menu
  def run(self):
    eval("menus."+self.menu).run()
  def back(self):
    eval("menus."+self.menu).back()
  def submit(self):
    eval("menus."+self.menu).submit()
  def left(self):
    eval("menus."+self.menu).left()
  def right(self):
    eval("menus."+self.menu).right()
  def up(self):
    eval("menus."+self.menu).up()
  def down(self):
    eval("menus."+self.menu).down()
  def text(self, atext):
    eval("menus."+self.menu).text(atext)
class Menu:
  def __init__(self, upmenu=MenuProxy("mainMenu")):
    self.upmenu = upmenu
  def run(self):
    data.background.blit()
  def back(self):
    if type(self.upmenu) == str:
      self.upmenu = eval("menus."+self.upmenu)
    data.currentmenu = self.upmenu
  def submit(self):
    pass
  def left(self):
    pass
  def right(self):
    pass
  def text(self, atext):
    pass
class ExitMenu(Menu):
  def run(self):
    print("Exited")
    sys.exit(0)
class ChoiceMenu(Menu):
  def __init__(self, upmenu, options):
    self.upmenu = upmenu
    self.currentoption = 0
    self.insubmenu = False
    self.submenuoption = 0
    self.options = options
  def back(self):
    if self.insubmenu:
      self.insubmenu = False
    else:
      if type(self.upmenu) == str:
        self.upmenu = eval("menus."+self.upmenu)
      data.currentmenu = self.upmenu
  def submit(self):
    if self.insubmenu:
      data.currentmenu = self.options[self.currentoption][2][self.submenuoption][1]
      self.insubmenu = False
    elif len(self.options[self.currentoption]) > 2:
      self.insubmenu = True
    else:
      data.currentmenu = self.options[self.currentoption][1]
  def left(self):
    if not self.currentoption-1 < 0:
      self.currentoption -= 1
    self.insubmenu = False
  def right(self):
    if not self.currentoption+1 >= len(self.options):
      self.currentoption += 1
    self.insubmenu = False
  def down(self):
    if len(self.options[self.currentoption]) > 2:
      if not self.submenuoption+1 >= len(self.options[self.currentoption][2]):
        self.submenuoption += 1
  def up(self):
    if len(self.options[self.currentoption]) > 2:
      if not self.submenuoption-1 < 0:
        self.submenuoption -= 1
  def run(self):
    data.background.blit()
    try:
      option = data.font.render(self.options[self.currentoption][0], True, (0,100,255))
    except IndexError:
      self.currentoption -= 1
      option = data.font.render(self.options[self.currentoption][0], True, (0,100,255))
    data.display.blit(option, (data.display.get_width()/2-option.get_width()/2, data.display.get_height()/2-option.get_height()/2))
    if not self.currentoption-1 < 0:
      leftoption = data.font.render(self.options[self.currentoption-1][0], True, (0,255,255))
      data.display.blit(leftoption, ((data.display.get_width()/2-option.get_width()/2)-(data.display.get_width()/2-leftoption.get_width()/2)/2, (data.display.get_height()/2-option.get_height()/2)))
    if not self.currentoption+1 >= len(self.options):
      rightoption = data.font.render(self.options[self.currentoption+1][0], True, (0,255,255))
      data.display.blit(rightoption, ((data.display.get_width()/2-option.get_width()/2)+(data.display.get_width()/2-rightoption.get_width()/2)/2, data.display.get_height()/2-option.get_height()/2))
    if not self.currentoption-2 < 0:
      leftoption = data.font.render(self.options[self.currentoption-2][0], True, (0,255,255))
      data.display.blit(leftoption, (0, (data.display.get_height()/2-option.get_height()/2)))
    if not self.currentoption+2 >= len(self.options):
      rightoption = data.font.render(self.options[self.currentoption+2][0], True, (0,255,255))
      data.display.blit(rightoption, ((data.display.get_width()-rightoption.get_width()), data.display.get_height()/2-option.get_height()/2))
    if self.insubmenu:
      x = (data.display.get_width()/2-option.get_width()/2)
      y = (data.display.get_height()/2-option.get_height()/2)+option.get_height()
      z = 0
      for i in self.options[self.currentoption][2]:
        if self.submenuoption == z:
          anoption = data.font.render(i[0], True, (0, 100, 255))
        else:
          anoption = data.font.render(i[0], True, (0, 255, 255))
        data.display.blit(anoption, (x, y))
        z += 1
        y += anoption.get_height()
class LaunchMenu(Menu):
  def __init__(self, upmenu, app, backup):
    self.app = app
    self.backup = backup
    self.upmenu = upmenu
  def run(self):
    print("Executing "+self.app)
    data.display = pygame.display.set_mode((0,0))
    if os.system(self.app+" "+data.sid) != 0: os.system(self.backup+" "+data.sid)
    data.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    if type(self.upmenu) == str:
      self.upmenu = eval("menus."+self.upmenu)
    data.currentmenu = self.upmenu