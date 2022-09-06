import ply.lex as lex

count_may = 0
count_min = 0
count_error = 0
t_ignore_ESPACIOS = r"[ ]+"

tokens = ["MAY", "MIN"] 

def t_MAY(t):
    r'[A-Z]+'
    global count_may
    count_may+=1
    return t

def t_MIN(t):
    r'[a-z]+'
    global count_min
    count_min+=1
    return t


def t_error(t):
    global count_error
    count_error +=1
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)
 
def t_newline(t):
  r'\n'
  t.lexer.lineno += 1

lexer = lex.lex()

data = input('Ingresar cadena: ')

lexer.input(data)

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"( {tok.type}, '{tok.value}' )")


print(f'Cantidad de repeticiones de count_min: {count_may}')
print(f'Cantidad de repeticiones de count_min: {count_min}')
print(f'Cantidad de repeticiones de count_error: {count_error}')