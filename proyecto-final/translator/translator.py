def translate(p,callback):
  with open("compi.ino","a+") as file:
    if (p):
      result = callback(p)
    file.write(result)