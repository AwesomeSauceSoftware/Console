import socket
import re
systemname = "ASSLab v2.0"
loginserver = ("localhost", 1670)
def login(u,p):
  data = ["Not Logged In", "", "0000000000"]
  s = socket.socket()
  s.connect(loginserver)
  s.send(b"LOGIN "+bytes(u, "utf-8")+b" "+bytes(p, "utf-8")+b"\n")
  data[0] = u
  data[1] = p
  data[2] = s.recv(10)
  s.close()
  if not re.match("000000000", str(data[2])):
    return data
  else:
    return False
def logout(sid):
  s = socket.socket()
  s.connect(loginserver)
  s.send(b"LOGOUT "+sid+b"\n")
  s.close()
def queryprivlevel(name):
  name = str(name)
  s = socket.socket()
  s.connect(loginserver)
  s.send(b"QUERY "+bytes(name, "utf-8")+b"\n")
  lvl = int(s.recv(2))
  s.close()
  return lvl
def getvalue(sid, key, length):
  sid = str(sid)
  key = str(key)
  s = socket.socket()
  s.connect(loginserver)
  s.send(b"GET "+bytes(sid, "utf-8")+b" "+bytes(key, "utf-8")+b"\n")
  value = s.recv(length)
  s.close()
  return value
def setvalue(sid, key, value):
  sid = str(sid)
  key = str(key)
  value = str(value)
  s = socket.socket()
  s.connect(loginserver)
  s.send(b"SET "+bytes(sid, "utf-8")+b" "+bytes(key, "utf-8")+b" "+bytes(value, "utf-8")+b"\n")
  s.close()
  return value