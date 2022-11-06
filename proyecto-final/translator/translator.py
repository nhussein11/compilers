def translate(p,callback,is_pin=False,is_first_pin=False):
  with open("compi.ino","r") as fileRead:
    file_content=fileRead.readlines()
    print("hola")
  with open("compi.ino","w") as file:
    if (p):
      if(is_pin):
        if(is_first_pin):
          new_file_content = file_content+["void setup(){\n"] + ["\n"] +["}\n"]
          index = new_file_content.index('\n')
          new_file_content.insert(index, callback(p))
          file.write("".join(new_file_content))
          return
        index = file_content.index('\n')
        file_content.insert(index, callback(p))
        file.write("".join(file_content))
        return
      file_content.append(callback(p))
      print(file_content)
      print("".join(file_content))
      file.write("".join(file_content))

 
  
#def write_void(file, file_content):
#  file.writelines(file_content+["void setup() {\n\n"+"}\n"])


  

