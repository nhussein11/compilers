def cb_p_librerias(p):
  list_cast = list(p)
  result = "".join(["#include <"]+list_cast[3:4]+[".h>"]+["\n"])
  return result



if __name__ == "__main__":
  res = cb_p_librerias([None, 'extend', '(', 'nombreDeLibreria', '.txt', ')', ';', None])
  print(res)