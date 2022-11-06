def translate(p,callback,is_first_pin=False):
  with open("compi.ino","a+") as file:
    if (p):
      result = callback(p)
    if (is_first_pin):
      file.write("void setup() {\n"+result+"}\n")
    file.write(result)