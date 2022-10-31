def translate(p,callback):
  with open("compi.ino","w+") as file:
    result = callback(p)
    file.write(result)
    