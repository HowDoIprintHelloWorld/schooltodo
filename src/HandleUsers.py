import base64

class UserHandler():
  def __init__(self):
    self.fileLoc = "users.txt"

  def check(self, userName):
    with open(self.fileLoc, "r") as file:
      return any([user for user in file.readlines() if userName == user.strip().lower()])

  def userFromCookie(self, cookieVal):
    return base64.b64decode(cookieVal).decode("utf-8")
    
  def loginCookie(self, cookieVal):
    return self.check(self.userFromCookie(cookieVal))

  def makeCookie(self, userName):
    return base64.b64encode(bytes(userName, "utf8"))

  def checkOff(self, cookieVal, indx):
    prev = self.getCheckedOff(cookieVal)
    if indx.strip() not in prev:
      with open("userdata/"+self.userFromCookie(cookieVal)+".txt", "a") as file:
        file.write(str(indx)+"\n")
    else:
      print(prev)
      prev.pop(prev.index(indx))
      with open("userdata/"+self.userFromCookie(cookieVal)+".txt", "w") as file:
        for part in prev:
          file.write(part+"\n")

  
  def getCheckedOff(self, cookieVal):
    with open("userdata/"+self.userFromCookie(cookieVal)+".txt", "r") as file:
      return [indx.strip() for indx in file.readlines()]