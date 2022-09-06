import ply.lex as lex

t_ignore_ESPACIOS = r"[ ]+"

tokens = ["NUMERO"]

def t_NUMERO(t):
    r'([0-9][0-9])+'
    return t

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)
 
def t_newline(t):
  r'\n'
  t.lexer.lineno += 1

data = input("ingresar: ")
lexer = lex.lex()
lexer.input(data)

count=0

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    if tok.type == 'NUMERO': count += 1
    print(f"( {tok.type}, '{tok.value}' )")

print(count)