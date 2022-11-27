def translate(p,callback,is_pin=False,is_first_pin=False,is_first_reserved=False, is_reserved=False):
  with open("compi.ino","r") as fileRead:
    file_content=fileRead.readlines()
  with open("compi.ino","w") as fileWrite:
    if (p):
      if(is_pin):
        if(is_first_pin):
          file_content+=['void setup(){\n'] + ['\n'] +['}\n']
        index = file_content.index('\n')
        file_content.insert(index, callback(p))
        fileWrite.write("".join(file_content))
        return
      if(is_reserved):
        if(is_first_reserved):
          file_content+=['void loop(){\n'] + ['\n'] +['}\n']
        index = file_content.index('\n',file_content.index('\n')+1)
        file_content.insert(index, callback(p))
        fileWrite.write("".join(file_content))
        return
      file_content.append(callback(p))
      fileWrite.write("".join(file_content))