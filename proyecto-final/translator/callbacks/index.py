def cb_p_librerias(p):
  list_cast = list(p)
  result = "".join(["#include \""]+list_cast[3:4]+[".h\""]+["\n"])
  return result

def cb_p_variable(p):
  list_cast = list(p)
  result = "".join([list_cast[5]]+[" "]+[list_cast[3]]+[";"]+["\n"])
  return result

def cb_p_asignacion(p):
  list_cast = list(p)
  result = "".join([list_cast[1]]+[" = "]+[str(list_cast[3])]+[";"]+["\n"])
  return result

if __name__ == "__main__":
  res = cb_p_librerias([None, 'extend', '(', 'nombreDeLibreria', '.txt', ')', ';', None])

  res1 = cb_p_variable([None, 'VBLE', '(', 'MD1', ':', 'int', ')', ';'])
  print(res1)