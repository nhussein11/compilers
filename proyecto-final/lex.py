import ply.lex as lex
from tokens import *

try:
    with open("prog-ejemplo.arducompi", "r") as file:
        data = file.read()
    lexer = lex.lex()
    lexer.input(data)
    print("Token - Lexema")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(f"( {tok.type}, '{tok.value}' )")
except IndexError:
    print("Error al leer el archivo")