def cb_p_librerias(p):
  list_cast = list(p)
  result = "".join(["#include <"]+list_cast[3:4]+[".h>"]+["\n"])
  return result

def cb_p_variable(p):
  list_cast = list(p)
  result = "".join([list_cast[5]]+[" "]+[list_cast[3]]+[";"]+["\n"])
  return result

def cb_p_asignacion(p):
  list_cast = list(p)
  result = "".join(["int "]+[list_cast[1]]+[" = "]+[str(list_cast[3])]+[";"]+["\n"])
  return result

def cb_p_condicional(p):
  list_cast = list(p)
  result = "".join(["if ("]+[") "]+ ["{"]+["\n"]+["}"]+["\n"])
  return result

def cb_p_procendimiento(p):
  list_cast = list(p)
  result = "".join([list_cast[6]]+[" "]+[list_cast[1]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
  return result

def cb_p_funcion(p):
  list_cast = list(p)
  result = "".join([list_cast[5]]+[list_cast[2]]+["()"]+["{"]+["\n"]+["}"]+["\n"])
  return result

def cb_p_comparacion(p):
  list_cast = list(p)
  result = "".join([list_cast[5]]+[" "]+[list_cast[3]]+["("]+[list_cast[7]]+[");"]+["\n"])
  return result


def cb_p_vpin(p):
   list_cast = list(p)
   result = "".join(["pinMode("]+[list_cast[3]]+[" , "]+[list_cast[5]]+[" );"]+["\n"])
   return result
def cb_p_reservadas(p):
  list_cast = list(p)
  reserved = ""
  if (list_cast[1] == "ADELANTE"):
    reserved  ="avanzar"
  if (list_cast[1] == "IZQUIERDA"):
    reserved  ="giro_izquierda"
  if (list_cast[1] == "FRENAR"):
    reserved  ="parar"
  if (list_cast[1] == "DERECHA"):
    reserved = "giro_derecha"
  if (list_cast[1] == "ESPERAR"):
    reserved = "delay"
  return "".join([reserved]+[list_cast[2]]+[list_cast[3]]+[";"]+["\n"])

if __name__ == "__main__":
  res = cb_p_librerias([None, 'extend', '(', 'nombreDeLibreria', '.txt', ')', ';', None])

  res1 = cb_p_variable([None, 'VBLE', '(', 'MD1', ':', 'int', ')', ';'])
  print(res1)