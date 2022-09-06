import ply.lex as lex

def t_MAY(t):
    r'[A-Z]+'
    return t

def t_MIN(t):
    r'[a-z]+'
    return t

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)
 
def t_newline(t):
  r'\n'
  t.lexer.lineno += 1

t_ignore_ESPACIOS = r"[ ]+"
tokens = ["MAY", "MIN"] 

data = input('Ingresar cadena: ')
lexer = lex.lex()
lexer.input(data)

count_may = 0
count_min = 0

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    if tok.type == 'MAX': count_may += 1
    if tok.type == 'MIN': count_min += 1
    print(f"( {tok.type}, '{tok.value}' )")

print(f'Cantidad de repeticiones de count_min: {count_may}')
print(f'Cantidad de repeticiones de count_min: {count_min}')