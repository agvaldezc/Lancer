# Lancer: Created by Alan Valdez & Rafael Manriquez

import ply.yacc as yacc

from LancerLex import tokens

#Reglas gramaticales expresadas en funciones
def p_expression_program(p):
    'program : PROGRAM ID SEMICOLON s1 s2 BLOCK'

def p_expression_program_s1(p):
    's1 : VARS | empty'

def p_expression_program_s2(p):
    '''s2 : FUNCTION s2
          | empty'''

def p_expression_vars(p):
    'vars : VAR s1 COLON type SEMICOLON s1'

def p_expression_vars_s1(p):
    '''s1 : ID
          | ID COMMA s1
          | empty'''

def p_expression_type(p):
    '''type : INT
            | FLOAT
            | BOOL
            | STRING
            | array'''

def p_expression_array(p):
    '''array : INT s1
             | FLOAT s1
             | STRING s1'''

def p_expression_array_s1(p):
    's1 : [ CTE-I ]'

def p_expression_block(p):
    'block : { s1 }'

def p_expression_block_s1(p):
    '''s1 : statue s1
          | empty'''

def p_expression_statue(p):
    '''statue : assignment
              | condition
              | read
              | write
              | cycle
              | functioncall
              | predefined
              | return'''

def p_expression_parameter(p):
    '''parameter : empty
                 | s1'''

def p_expression_parameter_s1(p):
    '''s1 : type ID
          | type ID COMMA s1'''

def p_expression_return(p):
    'return : RETURN ssexpression SEMICOLON'

def p_expression_assignment(p):
    'assignment : ID s1 = s2'

def p_expression_assignment_s1(p):
    '''s1 : empty
          | LBRACKET ssexpression RBRACKET'''

def p_expression_assignment_s2(p):
    '''s2 : functioncall
          | ssexpression'''

def p_expression_ssexpression(p):
    '''ssexpression : sexpression
                    | !! sexpression'''

def p_expression_sexpression(p):
    'sexpression : expression s1'

def p_expression_sexpression_s1(p):
    '''s1 : empty
          | && sexpression
          | || sexpression'''

def p_expression_expression(p):
    'expression : exp s1'

def p_expression_expression_s1(p):
    '''s1 : empty
          | GT exp
          | LT exp
          | ET exp
          | NE exp'''

def p_expression_term(p):
    'term : factor s1'

def p_expression_term_s1(p):
    '''s1 : empty
          | TIMES term
          | DIVISION term'''

def p_expression_exp(p):
    'exp : term s1'

def p_expression_exp_s1(p):
    '''s1 : empty
          | PLUS term
          | MINUS term'''

def p_expression_predefined(p):
    '''predefined : drawcircle
                  | drawsquare
                  | drawtriangle
                  | drawline
                  | drawpolygon
                  | drawcurve'''


def p_expression_factor(p):
    '''factor : '''

def p_expression_condition(p):
    'condition : IF s1 RPAREN block s3'

def p_expression_condition_s1(p):
    '''s1 : LPAREN s2
          | !! s2'''

def p_expression_condition_s2(p):
    '''s2 : ssexpression
          | functioncall'''

def p_expression_condition_s3(p):
    '''s3 : empty
          | ELSE block
          | s1'''

def p_expression_read(p):
    'read : ID EQUAL INPUT SEMICOLON'

def p_expression_write(p):
    '''write : PRINT LPAREN ssexpression RPAREN'''

def p_expression_color(p):
    '''color : RED
             | GREEN
             | BLUE
             | YELLOW
             | BROWN
             | BLACK'''

def p_expression_cycle(p):
    'cycle : WHILE LPAREN ssexpression RPAREN block'

def p_expression_function(p):
    'function : FUNC s1 ID LPAREN parameter RPAREN block'

def p_expression_function_s1(p):
    '''s1 : VOID
          | type'''

def p_expression_functioncall(p):
    'functioncall : ID LPAREN s1 RPAREN SEMICOLON'

def p_expression_functioncall_s1(p):
    '''s1 : empty
          | ssexpression
          | ssexpression COMMA s1'''


''' FALTAN LAS DE DRAW '''

#Error de sintaxis
def p_error(p):
    print("Syntax error in input!")

#Definicion de espacio vacio
def p_empty(p):
    'empty :'
    pass

#Construir el parser
parser = yacc.yacc(debug=1)

#Escribir el nombre o ruta del archivo a leer
print("Nombre o ruta dek archivo a analizar: ")
fileName = raw_input()

#Abrir archivo
file = open(fileName, 'r')
code = file.read()

#Imprimir codigo leido
print (code)

#Parsear el codigo leido del archivo
parser.parse(code)
# while True:
#    try:
#        s = raw_input()
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(code)
#    print(result)
