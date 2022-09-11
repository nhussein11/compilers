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
    "FRENAR": "FRENAR",
}

tokens = [
    "PARENTESIS",
    "COMA",
    "ID",
    "LIBRERIA",
    "VARTYPESEPARATOR",
    "TYPE",
    "NUMBER",
    "DECIMALNUMBER",
    "OPERADOR",
    "COMMENT",
] + list(reserved.values())


def t_VARTYPESEPARATOR(t):
    r":"
    return t


def t_TYPE(t):
    r"entero|texto|decimal|logico|INPUT|OUTPUT"
    return t


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_DECIMALNUMBER(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t


def t_OPERADOR(t):
    r"[+|-|*|>|<|>=|<=|==|!=|&&|.]"
    return t


def t_COMMENT(t):
    r"//.* | {*.*}"
    t.lineno += 1
    return t


def t_PARENTESIS(t):
    r"[\(|\)]+"
    return t


def t_COMA(t):
    r","
    return t


def t_newline(t):
    r";\n|\n|;"
    t.lexer.lineno += 1


def t_error(t):
    print(
        "Se encontró un error: %s" % repr(t.value[0]) + " en la linea " + str(t.lineno)
    )
    t.lexer.skip(1)
