from ply import yacc
from lex import tokens, analizador_lexico
from translator.callbacks.index import *
from translator.translator import translate
is_setup = False
def p_programa(p):
  """programa : INICIODEPROGRAMA declaraciones FINPROGRAMA"""
  pass
def p_declaraciones(p):
  """declaraciones : librerias cuerpo
                    | cuerpo"""
  pass
def p_librerias(p):
  """ librerias : LIBRERIA PARENTESISA ID EXTENSION PARENTESISC COMA librerias
                | LIBRERIA PARENTESISA ID EXTENSION PARENTESISC ENDOFLINE"""
  translate(p,cb_p_librerias)
  pass

def p_cuerpo(p):
  """ cuerpo : variable cuerpo
            | funcion cuerpo
            | asignacion cuerpo
            | procedimiento cuerpo
            | condicional cuerpo
            | bucle cuerpo
            | reservadas cuerpo
            | vpin cuerpo
            | empty"""
  pass
def p_vpin(p):
  """vpin : VPIN PARENTESISA ID VARTYPESEPARATOR TYPEVPIN PARENTESISC ENDOFLINE"""
  translate(p,cb_p_vpin)
  pass
def p_reservadas(p):
  """ reservadas : ADELANTE PARENTESISA PARENTESISC ENDOFLINE
                | ATRAS PARENTESISA  PARENTESISC ENDOFLINE
                | IZQUIERDA PARENTESISA  PARENTESISC ENDOFLINE
                | DERECHA PARENTESISA PARENTESISC ENDOFLINE
                | ESPERAR PARENTESISA NUMBER PARENTESISC ENDOFLINE
                | ESPERAR PARENTESISA ID PARENTESISC ENDOFLINE
                | FRENAR PARENTESISA PARENTESISC ENDOFLINE"""
  pass
def p_bucle(p):
  """bucle : WHILE PARENTESISA  comparacion PARENTESISC BEGIN cuerpo END ENDOFLINE"""
  pass
def p_condicional(p):
  """condicional : IF PARENTESISA comparacion PARENTESISC BEGIN cuerpo END ENDOFLINE
                 | IF PARENTESISA  comparacion PARENTESISC BEGIN cuerpo END ELSE BEGIN cuerpo END ENDOFLINE"""
  #translate(p,cb_p_condicional)
  pass
def p_procedimiento(p):
  """procedimiento : PROCEDIMIENTO ID PARENTESISA argumentos PARENTESISC ENDOFLINE"""
  translate(p,cb_p_procendimiento)
  pass
def p_asignacion(p):
  """asignacion : ID IGUAL ID ENDOFLINE 
                  | ID IGUAL NUMBER ENDOFLINE  
                  | ID IGUAL DECIMALNUMBER ENDOFLINE 
                  | ID IGUAL BOOLEANS ENDOFLINE 
                  """
  translate(p,cb_p_asignacion)
  pass
def p_comparacion(p):
  """comparacion : ID OPERADOR ID
                  | ID OPERADOR NUMBER
                  | ID OPERADOR DECIMALNUMBER
                  | ID OPERADOR BOOLEANS
                  | NUMBER OPERADOR ID
                  | NUMBER OPERADOR NUMBER
                  | NUMBER OPERADOR DECIMALNUMBER
                  | NUMBER OPERADOR BOOLEANS
                  | DECIMALNUMBER OPERADOR ID
                  | DECIMALNUMBER OPERADOR NUMBER
                  | DECIMALNUMBER OPERADOR DECIMALNUMBER
                  | DECIMALNUMBER OPERADOR BOOLEANS
                  | BOOLEANS OPERADOR ID
                  | BOOLEANS OPERADOR NUMBER
                  | BOOLEANS OPERADOR DECIMALNUMBER
                  | BOOLEANS OPERADOR BOOLEANS"""
  pass


def p_funcion(p):
  """funcion : FUNCION ID PARENTESISA argumentos PARENTESISC VARTYPESEPARATOR TYPE ENDOFLINE"""
  translate(p,cb_p_funcion)
  pass
def p_variable(p):
  """variable : VARIABLE PARENTESISA ID  VARTYPESEPARATOR TYPE PARENTESISC ENDOFLINE"""
  translate(p,cb_p_variable)
  pass
def p_argumentos(p):
  """ argumentos : ID VARTYPESEPARATOR TYPE COMA argumentos
                 | ID VARTYPESEPARATOR TYPE"""
  pass

def p_empty(p):
  'empty :'
  pass
def p_error(p):
  print("Error sintÃ¡ctico en la li­nea: " + str(p.lineno)
              + ". No se esperaba el token: " + str(p.value))
  raise Exception('syntax', 'error')

analizador_lexico.lineno = 0
analizador_sintactico = yacc.yacc()