from unittest import skip
from ply import lex
reserved = {
    "PINICIO": "INICIODEPROGRAMA",
    "PEND": "FINPROGRAMA",
    "extend": "LIBRERIA",
    "VBLE": "VARIABLE",
    "FUN": "FUNCION",
    "PROC": "PROCEDIMIENTO",
    "VPIN": "VPIN",
    "BEGIN": "BEGIN",
    "END": "END",
    "IF": "IF",
    "ELSE": "ELSE",
    "WHILE": "WHILE",
    "ADELANTE": "ADELANTE",
    "ATRAS": "ATRAS",
    "IZQUIERDA": "IZQUIERDA",
    "DERECHA": "DERECHA",
    "ESPERAR": "ESPERAR",
    "FRENAR": "FRENAR"}

tokens = [
    "PARENTESISA",
    "PARENTESISC",
    "COMA",
    "ID",
    "VARTYPESEPARATOR",
    "TYPE",
    "NUMBER",
    "DECIMALNUMBER",
    "OPERADOR",
    "OPERADORPUNTO",
    "IGUAL",
    "COMMENT",
    "ENDOFLINE",
    "EXTENSION"
] + list(reserved.values())


def t_VARTYPESEPARATOR(t):
    r":"
    return t


def t_TYPE(t):
    r"int|string|float|bool|INPUT|OUTPUT"
    return t

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_IGUAL(t):
    r"="
    return t
def t_DECIMALNUMBER(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t
def t_EXTENSION(t):
    r"Extension"
    return t
def t_OPERADORPUNTO(t):
    r'\.'
    return t
def t_OPERADOR(t):
    r"[+|-|*|>|<|>=|<=|==|!=|&&]"
    return t


def t_COMMENT(t):
    r"//.* | {\*.\*}"
    t.lineno += 1
    t.lexer.skip(1)


def t_PARENTESISA(t):
    r"\("
    return t

def t_PARENTESISC(t):
    r"\)"
    return t  
def t_COMA(t):
    r","
    return t

def t_ENDOFLINE(t):
    r";"
    return t
def t_newline(t):
    r"\n"
    t.lexer.lineno += 1


def t_error(t):
    print(
        "Se encontró un error: %s" % repr(t.value[0]) + " en la linea " + str(t.lineno)
    )
    t.lexer.skip(1)
def t_space(t):
    r'\s+'
    pass
def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9]*"
    t.type = reserved.get(t.value, "ID")
    return t

analizador_lexico = lex.lex()
