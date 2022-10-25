
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADELANTE ATRAS BEGIN COMA COMMENT DECIMALNUMBER DERECHA ELSE END ENDOFLINE ESPERAR EXTENSION FINPROGRAMA FRENAR FUNCION ID IF IGUAL INICIODEPROGRAMA IZQUIERDA LIBRERIA NUMBER OPERADOR OPERADORPUNTO PARENTESISA PARENTESISC PROCEDIMIENTO TYPE VARIABLE VARTYPESEPARATOR VPIN WHILEprograma : INICIODEPROGRAMA declaraciones FINPROGRAMAdeclaraciones : librerias\n                   | cuerpo librerias : LIBRERIA PARENTESISA ID OPERADORPUNTO EXTENSION PARENTESISC COMA librerias\n                | LIBRERIA PARENTESISA ID OPERADORPUNTO EXTENSION PARENTESISC ENDOFLINE cuerpo cuerpo : variable cuerpo\n            | funcion cuerpo\n            | asignacion cuerpo\n            | emptyasignacion : ID IGUAL ID ENDOFLINEfuncion : FUNCION ID PARENTESISA argumentos PARENTESISC VARTYPESEPARATOR TYPE ENDOFLINEvariable : VARIABLE PARENTESISA ID  VARTYPESEPARATOR TYPE PARENTESISC ENDOFLINE argumentos : ID VARTYPESEPARATOR TYPE COMA argumentos\n                 | ID VARTYPESEPARATOR TYPEempty :'
    
_lr_action_items = {'INICIODEPROGRAMA':([0,],[2,]),'$end':([1,14,],[0,-1,]),'LIBRERIA':([2,39,],[6,6,]),'VARIABLE':([2,8,9,10,27,40,41,47,],[12,12,12,12,-10,12,-12,-11,]),'FUNCION':([2,8,9,10,27,40,41,47,],[13,13,13,13,-10,13,-12,-11,]),'ID':([2,8,9,10,13,15,16,20,25,27,40,41,42,47,],[7,7,7,7,21,22,23,24,29,-10,7,-12,29,-11,]),'FINPROGRAMA':([2,3,4,5,8,9,10,11,17,18,19,27,40,41,44,45,47,],[-15,14,-2,-3,-15,-15,-15,-9,-6,-7,-8,-10,-15,-12,-4,-5,-11,]),'PARENTESISA':([6,12,21,],[15,20,25,]),'IGUAL':([7,],[16,]),'OPERADORPUNTO':([22,],[26,]),'ENDOFLINE':([23,35,36,43,],[27,40,41,47,]),'VARTYPESEPARATOR':([24,29,34,],[28,33,38,]),'EXTENSION':([26,],[31,]),'TYPE':([28,33,38,],[32,37,43,]),'PARENTESISC':([30,31,32,37,46,],[34,35,36,-14,-13,]),'COMA':([35,37,],[39,42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'declaraciones':([2,],[3,]),'librerias':([2,39,],[4,44,]),'cuerpo':([2,8,9,10,40,],[5,17,18,19,45,]),'variable':([2,8,9,10,40,],[8,8,8,8,8,]),'funcion':([2,8,9,10,40,],[9,9,9,9,9,]),'asignacion':([2,8,9,10,40,],[10,10,10,10,10,]),'empty':([2,8,9,10,40,],[11,11,11,11,11,]),'argumentos':([25,42,],[30,46,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INICIODEPROGRAMA declaraciones FINPROGRAMA','programa',3,'p_programa','yacc.py',6),
  ('declaraciones -> librerias','declaraciones',1,'p_declaraciones','yacc.py',9),
  ('declaraciones -> cuerpo','declaraciones',1,'p_declaraciones','yacc.py',10),
  ('librerias -> LIBRERIA PARENTESISA ID OPERADORPUNTO EXTENSION PARENTESISC COMA librerias','librerias',8,'p_librerias','yacc.py',13),
  ('librerias -> LIBRERIA PARENTESISA ID OPERADORPUNTO EXTENSION PARENTESISC ENDOFLINE cuerpo','librerias',8,'p_librerias','yacc.py',14),
  ('cuerpo -> variable cuerpo','cuerpo',2,'p_cuerpo','yacc.py',18),
  ('cuerpo -> funcion cuerpo','cuerpo',2,'p_cuerpo','yacc.py',19),
  ('cuerpo -> asignacion cuerpo','cuerpo',2,'p_cuerpo','yacc.py',20),
  ('cuerpo -> empty','cuerpo',1,'p_cuerpo','yacc.py',21),
  ('asignacion -> ID IGUAL ID ENDOFLINE','asignacion',4,'p_asignacion','yacc.py',24),
  ('funcion -> FUNCION ID PARENTESISA argumentos PARENTESISC VARTYPESEPARATOR TYPE ENDOFLINE','funcion',8,'p_funcion','yacc.py',27),
  ('variable -> VARIABLE PARENTESISA ID VARTYPESEPARATOR TYPE PARENTESISC ENDOFLINE','variable',7,'p_variable','yacc.py',30),
  ('argumentos -> ID VARTYPESEPARATOR TYPE COMA argumentos','argumentos',5,'p_argumentos','yacc.py',33),
  ('argumentos -> ID VARTYPESEPARATOR TYPE','argumentos',3,'p_argumentos','yacc.py',34),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',38),
]
