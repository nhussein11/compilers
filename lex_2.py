import ply.lex as lex

count = 0
t_ignore_ESPACIOS = r"[ ]+"

tokens = ["MB"]


def t_MB(t):
    r"[a-zA-Z]*(mb|MB)+[a-zA-Z]*"
    global count
    count += 1
    return t


def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)


def t_newline(t):
    r"\n"
    t.lexer.lineno += 1


lexer = lex.lex()

data = input("Ingresar cadena: ")

lexer.input(data)

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"( {tok.type}, '{tok.value}' )")

print(f"Cantidad de repeticiones de count: {count}")
