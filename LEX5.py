import ply.lex as lex

t_ignore_ESPACIOS = r"[ ]+"

count=0

tokens = ["NUMERO"]

def t_NUMERO(t):
    r'([0-9][0-9])+'
    global count
    count += 1
    return t

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)
 
def t_newline(t):
  r'\n'
  t.lexer.lineno += 1

lexer = lex.lex()

data = input("ingresar: ")
lexer.input(data)

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"( {tok.type}, '{tok.value}' )")
print(count)