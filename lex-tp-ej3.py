import ply.lex as lex

def t_CERO(t):
    r'[0][a-zA-Z_0-9]*(11)'
    return t

def t_UNO(t):
    r'[1][a-zA-Z_0-9]*(00)'
    return t

def t_error(t):
    print("Se encontró un error: %s" % repr(t.value[0]))
    t.lexer.skip(1)
 
tokens = ["CERO","UNO"] 
t_ignore_ESPACIOS = r"[ ]+"
lexer = lex.lex()

data = input('Ingresar cadena: ')

lexer.input(data)

count_cero = 0
count_uno = 0

print("Token - Lexema")
while True:
    tok = lexer.token()
    if not tok:
        break
    if tok.type == 'CERO': count_cero += 1
    if tok.type == 'UNO': count_uno += 1
    print(f"( {tok.type}, '{tok.value}' )")

print(f'Cantidad de ceros: {count_cero}')
print(f'Cantidad de unos: {count_uno}')