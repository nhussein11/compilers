from ply import yacc
from lex import tokens,analizador_lexico


def p_programa(p):
  """programa : INICIODEPROGRAMA declaraciones FINPROGRAMA"""
  pass
def p_declaraciones(p):
  """declaraciones : librerias
                   | cuerpo"""
  pass
def p_librerias(p):
  """ librerias : LIBRERIA PARENTESISA ID OPERADORPUNTO EXTENSION PARENTESISC COMA librerias
                | LIBRERIA PARENTESISA ID OPERADORPUNTO EXTENSION PARENTESISC ENDOFLINE cuerpo"""
  pass

def p_cuerpo(p):
  """ cuerpo : VARIABLE PARENTESISA ID  VARTYPESEPARATOR TYPE PARENTESISC ENDOFLINE cuerpo
            | FUNCION ID PARENTESISA argumentos PARENTESISC VARTYPESEPARATOR TYPE ENDOFLINE cuerpo
            | empty"""
  pass
def p_argumentos(p):
  """ argumentos : ID VARTYPESEPARATOR TYPE COMA argumentos
                 | ID VARTYPESEPARATOR TYPE"""
  pass

def p_empty(p):
  'empty :'
  pass
analizador_sintactico = yacc.yacc()
analizador_lexico.lineno = 0