import ply.lex as lex

def t_HTML(t):
    r'(<HTML>)'
    return t

def t_HEAD(t):
    r'(<HEAD>)|(</HEAD>)'
    return t

def t_TITLE(t):
    r'(<TITLE>)|(</TITLE>)'
    return t

def t_CARACTER(t):
    r'[a-zA-Z_][a-zA-Z0-9_À-ÿ]*'
    return t

def t_BODY(t):
    r'(<BODY>)|(</BODY>)'
    return t

def t_PARAGRAPH(t):
    r'(<P>)|(</P>)'
    return t

def t_BOLD(t):
    r'(<B>)|(</B>)'
    return t

def t_HR(t):
    r'(<HR>)'
    return t

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)

def t_newline(t):
  r'\n'
  t.lexer.lineno += 1
 
tokens = [
    "HTML", 
    "HEAD",
    "TITLE", 
    "CARACTER", 
    "BODY", 
    "PARAGRAPH", 
    "BOLD", 
    "HR"
] 

t_ignore_ESPACIOS = r"[ ]+"

lexer = lex.lex()

filename = './ejemplo-html.txt'

try:
    f = open(filename)
    data = f.read()
    f.close()   
    
except IndexError:
    print('Error al leer el archivo')
    data=''

lexer.input(data)

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"( {tok.type}, '{tok.value}' )")