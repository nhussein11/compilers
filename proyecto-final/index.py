from yacc import analizador_sintactico
try:
  with open("test1.txt", "r") as file:
    data = file.read()
    try:
      analizador_sintactico.parse(data)
      print("Analsis correcto")
    except Exception:
      print("Analisis Incorrecto")
except IndexError:
  print("Error al leer el archivo")