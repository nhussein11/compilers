import ply.lex as lex

def t_MB(t):
    r"[a-zA-Z]*(mb|MB)+[a-zA-Z]*"
    return t

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)

def t_newline(t):
    r"\n"
    t.lexer.lineno += 1

t_ignore_ESPACIOS = r"[ ]+"
tokens = ["MB"]

data = input("Ingresar cadena: ")
lexer = lex.lex()
lexer.input(data)

count = 0

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    if tok.type == 'MB': count += 1
    print(f"( {tok.type}, '{tok.value}' )")

print(f"Cantidad de repeticiones de count: {count}")
