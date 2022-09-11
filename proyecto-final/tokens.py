import ply.lex as lex

tokens = ["INICIOPROGRAMA", "FINPROGRAMA", "PARENTESIS", "COMA", "EXTEND", "ID", "LIBRERIA", "VARIABLE", "VARTYPESEPARATOR", "TYPE", "NUMBER", "DECIMALNUMBER", "OPERADOR", "FUN", "PROC", "VPIN",
          "COMMENT", "BEGIN", "END", "IF", "ELSE", "WHILE", "ADELANTE", "ATRAS", "IZQUIERDA", "DERECHA", "ESPERAR", "FRENAR"]


def t_INICIOPROGRAMA(t):
    r"PINICIO"
    return t


def t_FINPROGRAMA(t):
    r"PEND"
    return t


def t_EXTEND(t):
    r"EXTEND"
    return t


def t_VARIABLE(t):
    r"VBLE"
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t


def t_VARTYPESEPARATOR(t):
    r":"
    return t


def t_TYPE(t):
    r"int|float|String|bool|INPUT|OUTPUT"
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_DECIMALNUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_OPERADOR(t):
    r'[+|-|*|>|<|>=|<=|==|!=|&&|.]'
    return t


def t_FUN(t):
    r"FUN"
    return t


def t_PROC(t):
    r"PROC"
    return t


def t_VPIN(t):
    r"VPIN"
    return t


def t_COMMENT(t):
    r"//.* | {*.*}"
    t.lineno += 1
    return t


def t_BEGIN(t):
    r"BEGIN"
    return t


def t_END(t):
    r"END"
    return t


def t_IF(t):
    r"IF"
    return t


def t_ELSE(t):
    r"ELSE"
    return t


def t_WHILE(t):
    r"WHILE"
    return t


def t_ADELANTE(t):
    r"ADELANTE"
    return t


def t_ATRAS(t):
    r"ATRAS"
    return t


def t_IZQUIERDA(t):
    r"IZQUIERDA"
    return t


def t_DERECHA(t):
    r"DERECHA"
    return t


def t_ESPERAR(t):
    r"ESPERAR"
    return t


def t_FRENAR(t):
    r"FRENAR"
    return t


def t_PARENTESIS(t):
    r'[\(|\)]+'
    return t


def t_COMA(t):
    r','
    return t


def t_newline(t):
    r';\n|\n|;'
    t.lexer.lineno += 1


def t_error(t):
    print("Se encontró un error: %s" %
          repr(t.value[0]) + " en la linea " + str(t.lineno))
    t.lexer.skip(1)


try:
    with open('prog-ejemplo.arducompi', "r") as file:
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
    print('Error al leer el archivo')
