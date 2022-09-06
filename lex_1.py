import ply.lex as lex

reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_OPERADOR(t):
    r'[\+|\*]+'
    return t

def t_PARENTESIS(t):
    r'[\(|\)]+'
    return t

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)
 
def t_newline(t):
  r'\n'
  t.lexer.lineno += 1

def t_ignore_ESPACIOS(t):
    r'[ ]+'
    pass

tokens = ["ID", "NUMERO", "OPERADOR", "PARENTESIS"] + list(reserved.values())

filename = './ejemplo.txt'

try:
    f = open(filename)
    data = f.read()
    f.close()   
    
except IndexError:
    print('Error al leer el archivo')
    data=''

lexer = lex.lex()
lexer.input(data)

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"( {tok.type}, '{tok.value}' )")
