# Lancer: Created by Alan Valdez & Rafael Manriquez

from LancerLex import tokens
import ply.yacc as yacc
import sys

#Reglas gramaticales expresadas en funciones
def p_expression_program(p):
    'program : PROGRAMA MAIN SEMICOLON prs1 prs2 block'
    print("Correct Sintax.")


def p_expression_prs1(p):
    '''prs1 : vars
            | empty'''

def p_expression_prs2(p):
    '''prs2 : function prs2
            | empty'''

def p_expression_vars(p):
    'vars : VAR vas1 COLON type SEMICOLON vas1'

def p_expression_vas1(p):
    '''vas1 : ID
            | ID COMA vas1
            | empty'''

#def p_expression_(p):
#	'''to_var_table :'''
	#print p[-1]
#	varid = p[-1]
	#print varid
#	if varid not in varTable['global'] and varid not in varTable[scope[len(scope)-1]]:
#		ids.add(varid)
#		varTable[scope[len(scope)-1]][varid]  = p[-3]
#	else:
#		print('Variable "%s" already registered' % (varid))
#		sys.exit()
#print dirProcedures[scope[len(scope)-1]]

def p_expression_type(p):
    '''type : INT_TYPE
            | FLOAT_TYPE
            | BOOL_TYPE
            | STRING_TYPE
            | array'''

def p_expression_array(p):
    '''array : INT_TYPE ars1
             | FLOAT_TYPE ars1
             | STRING_TYPE ars1'''

def p_expression_ars1(p):
    'ars1 : LARRAY CTEI RARRAY'

def p_expression_block(p):
    'block : LBRACKET bls1 RBRACKET'

def p_expression_bls1(p):
    '''bls1 : statue bls1
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
                 | pas1'''

def p_expression_pas1(p):
    '''pas1 : type ID
          | type ID COMA pas1'''

def p_expression_return(p):
    'return : RETURN ssexpression SEMICOLON'

def p_expression_assignment(p):
    'assignment : ID ass1 ASSIGN ass2 SEMICOLON'

def p_expression_ass1(p):
    '''ass1 : empty
          | LARRAY ssexpression RARRAY'''

def p_expression_ass2(p):
    '''ass2 : functioncall
          | ssexpression'''

def p_expression_ssexpression(p):
    '''ssexpression : sexpression
                    | NOT sexpression'''

def p_expression_sexpression(p):
    'sexpression : expression ses1'

def p_expression_ses1(p):
    '''ses1 : empty
          | AND sexpression
          | OR sexpression'''

def p_expression_expression(p):
    'expression : exp exs1'

def p_expression_exs1(p):
    '''exs1 : empty
          | GT exp
          | LT exp
          | GE exp
          | LE exp
          | EQUAL exp
          | DIFFERENT exp'''

def p_expression_term(p):
    'term : factor tes1'

def p_expression_tes1(p):
    '''tes1 : empty
          | TIMES factor tes1
          | DIVISION factor tes1'''

def p_expression_exp(p):
    'exp : term exps1'

def p_expression_exps1(p):
    '''exps1 : empty
          | PLUS term exps1
          | MINUS term exps1'''

def p_expression_predefined(p):
    '''predefined : drawcircle
                  | drawsquare
                  | drawtriangle
                  | drawline
                  | drawpolygon
                  | drawcurve'''

def p_expression_condition(p):
    'condition : IF cos1 RPAREN block cos3'

def p_expression_cos1(p):
    '''cos1 : LPAREN cos2
          | NOT cos2'''

def p_expression_cos2(p):
    '''cos2 : ssexpression
          | functioncall'''

def p_expression_cos3(p):
    '''cos3 : ELSE block
            | empty'''

def p_expression_read(p):
    'read : ID ASSIGN INPUT SEMICOLON'

def p_expression_write(p):
    '''write : PRINT LPAREN ssexpression RPAREN SEMICOLON'''

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
    'function : FUNC fus1 ID LPAREN parameter RPAREN block'

def p_expression_fus1(p):
    '''fus1 : VOID
          | type'''

def p_expression_functioncall(p):
    'functioncall : ID LPAREN fcs1 RPAREN SEMICOLON'

def p_expression_fcs1(p):
    '''fcs1 : empty
          | ssexpression
          | ssexpression COMA fcs1'''

def p_expression_drawline(p):
    'drawline : DRAWLINE LPAREN ssexpression COMA ssexpression COMA ssexpression COMA ssexpression COMA color RPAREN SEMICOLON'

def p_expression_drawsquare(p):
    'drawsquare : DRAWSQUARE LPAREN ssexpression COMA ssexpression COMA color RPAREN SEMICOLON'

def p_expression_drawcircle(p):
    'drawcircle : DRAWCIRCLE LPAREN ssexpression COMA ssexpression COMA color RPAREN SEMICOLON'

def p_expression_drawtriangle(p):
    'drawtriangle : DRAWTRIANGLE LPAREN ssexpression COMA ssexpression COMA color RPAREN SEMICOLON'

def p_expression_drawcurve(p):
    'drawcurve : DRAWCURVE LPAREN ssexpression COMA color RPAREN SEMICOLON'

def p_expression_drawpolygon(p):
    'drawpolygon : DRAWPOLYGON LPAREN ssexpression COMA ssexpression COMA color RPAREN SEMICOLON'

def p_expression_factor(p):
    '''factor : fact'''

def p_expression_fact(p):
    '''fact : LPAREN ssexpression RPAREN
            | sign constant'''

def p_expression_sign(p):
    '''sign : PLUS
            | MINUS
            | empty'''

def p_expression_constant(p):
    '''constant : ID const
                 | CTEI
                 | CTEF'''

def p_expression_const(p):
    '''const : LARRAY ssexpression RARRAY
             | LPAREN ssexpression RPAREN
             | empty'''

def p_expression_fas1(p):
    '''fas1 : ID fas2
              | CTEI
              | CTEF'''

def p_expression_fas2(p):
    '''fas2 : LARRAY exp RARRAY
              | LPAREN exp RPAREN
              | empty'''

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
print("Nombre o ruta del archivo a analizar: ")
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