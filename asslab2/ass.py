import default
import pygame
import data
import socket
import asscore
class AccountsMenu(default.ChoiceMenu):
  def __init__(self, upmenu):
    default.ChoiceMenu.__init__(self, upmenu, [("Back", default.MenuProxy("mainMenu")), ("Login", LoginMenu(self)), ("Register", RegisterMenu(self))])
    data.username = "Not Logged In"
  def run(self):
    default.ChoiceMenu.run(self)
  def login(self, u, p):
    d = asscore.login(u, p)
    if (d != False):
      data.username = d[0]
      data.password = d[1]
      data.sid = d[2]
      self.options = [("Back", default.MenuProxy("mainMenu")), ("Logout", LogoutMenu(self))]
    else:
      self.logout()
  def logout(self):
    asscore.logout(data.sid)
    data.username = "Not Logged In"
    data.password = ""
    data.sid = "0000000000"
    self.options = [("Back", default.MenuProxy("mainMenu")), ("Login", LoginMenu(self)), ("Register", RegisterMenu(self))]
class RegisterMenu(default.Menu):
  def __init__(self, upmenu):
    default.Menu.__init__(self, upmenu)
    self.done = False
  def run(self):
    if not self.done:
      data.currentmenu = LoginMenu(self)
      self.done = True
    else:
      data.currentmenu = self.upmenu
  def login(self, u, p):
    s = socket.socket()
    s.connect(("localhost", 1670))
    s.send(b"REGISTER "+bytes(u, "utf-8")+b" "+bytes(p, "utf-8")+b"\n")
    s.close()
    self.upmenu.login(u, p)
class LogoutMenu(default.Menu):
  def run(self):
    self.upmenu.logout()
    data.currentmenu = self.upmenu
class LoginMenu(default.Menu):
  def __init__(self, upmenu):
    default.Menu.__init__(self, upmenu)
    self.stage = 0
    self.atext = ""
    self.username = ""
    self.password = ""
  def text(self, atext):
    self.atext = self.atext+atext
  def left(self):
    self.atext = self.atext+"a"
  def right(self):
    self.atext = self.atext+"d"
  def up(self):
    self.atext = self.atext+"w"
  def down(self):
    self.atext = self.atext+"s"
  def submit(self):
    if self.stage == 0:
      if len(self.atext) > 5:
        self.username = self.atext
        self.atext = ""
        self.stage = 1
        print("Submitted.")
    elif self.stage == 1:
      print("Submitted Again.")
      self.password = self.atext
      self.upmenu.login(self.username, self.password)
      data.currentmenu = self.upmenu
  def back(self):
    self.atext = self.atext[:len(self.atext)-1]
  def run(self):
    data.background.blit()
    if self.stage == 0:
      usernamefield = data.font.render("Username: "+self.atext, True, (0,255,255))
      data.display.blit(usernamefield, (data.display.get_width()/2-usernamefield.get_width()/2, 10))
    if self.stage == 1:
      usernamefield = data.font.render("Username: "+self.username, True, (0,255,255))
      data.display.blit(usernamefield, (data.display.get_width()/2-usernamefield.get_width()/2, 10))
      passwordfield = data.font.render("Password: "+("*"*len(self.atext)), True, (0,255,255))
      data.display.blit(passwordfield, (data.display.get_width()/2-usernamefield.get_width()/2, 50))