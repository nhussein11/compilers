def translate(p,callback):
  with open("compi.ino","a+") as file:
    result = callback(p)
    file.write(result)
    