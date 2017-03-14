#Alan Gustavo Valdez Cascajares A01336955
#Rafael Manrriquez Valdez

import ply.yacc as yacc
import sys as sys
from LancerLex import tokens
from Directories.FunctionDirectory import FunctionDirectory

funcDir = FunctionDirectory()
currentScope = ""

#Reglas gramaticales expresadas en funciones
def p_expression_programa(p):
    'prog : PROGRAMA ID create_func_dir SEMICOLON vars function bloque'
    print('Correct Syntax.')

def p_expression_create_func_dir(p):
    'create_func_dir : '

    #Save current function name (scope)
    global currentScope
    currentScope = p[-1]

    #Create function directory variable
    funcDir.addFunction(currentScope, 'void')


def p_expression_vars(p):
    '''vars : VAR ID array COLON type add_var SEMICOLON masvars
            | empty'''

def p_expression_add_var(p):
    'add_var : '

    global currentScope

    varName = p[-4]
    varType = p[-1]

    if funcDir.addFunctionVariable(currentScope, varName, varType):
        funcDir.addParameterTypes(currentScope, [varType])
    else:
        sys.exit(-1)

def p_expression_type(p):
    '''type : INT_TYPE
            | FLOAT_TYPE
            | STRING_TYPE
            | BOOL_TYPE
            | array'''
    p[0] = p[1]

def p_expression_array(p):
    '''array : LARRAY ss_expression RARRAY
             | empty'''

def p_expression_masvars(p):
    '''masvars : ID COLON type add_masvars SEMICOLON masvars
                | empty'''

def p_expression_add_masvars(p):
    'add_masvars : '
    global currentScope

    varName = p[-3]
    varType = p[-1]

    if funcDir.addFunctionVariable(currentScope, varName, varType):
        funcDir.addParameterTypes(currentScope, [varType])
    else:
        sys.exit(-1)

def p_expression_function(p):
    '''function : FUNC func_type ID add_to_func_dir LPAREN parameters RPAREN bloque function
                | empty'''

def p_expression_func_type(p):
    '''func_type : VOID
                 | type'''
    p[0] = p[1]

def p_expression_add_to_func_dir(p):
    'add_to_func_dir : '

    global currentScope

    funcName = p[-1]
    funcType = p[-2]

    if not funcDir.functionExists(funcName):
        currentScope = funcName
        funcDir.addFunction(funcName, funcType)
    else:
        sys.exit(-1)

def p_expression_parameters(p):
    '''parameters : type ID add_params array more_params
                  | empty'''

def p_expression_more_params(p):
    '''more_params : COMA type ID add_params more_params
                   | empty'''

def p_expression_add_params(p):
    'add_params : '

    global currentScope

    paramName = p[-1]
    paramType = p[-2]

    if funcDir.addFunctionVariable(currentScope, paramName, paramType):
        funcDir.addParameterTypes(currentScope, [paramType])

def p_expression_bloque(p):
    'bloque : LBRACKET est RBRACKET'

def p_expression_est(p):
    '''est : estatuto est
            | empty'''

def p_expression_estatuto(p):
    '''estatuto : asignacion
                | escritura
                | condicion
                | lectura
                | ciclo
                | voidfunction
                | functioncall
                | predefined
                | return'''

def p_expression_return(p):
    'return : RETURN ss_expression SEMICOLON'

def p_expression_predefined(p):
    '''predefined : drawcircle
                  | drawsquare
                  | drawtriangle
                  | drawline
                  | drawpolygon
                  | drawcurve'''

def p_expression_color(p):
    '''color : RED
             | GREEN
             | BLUE
             | YELLOW
             | BROWN
             | BLACK'''

def p_expression_drawline(p):
    'drawline : DRAWLINE LPAREN ss_expression COMA ss_expression COMA ss_expression COMA ss_expression COMA color RPAREN SEMICOLON'

def p_expression_drawsquare(p):
    'drawsquare : DRAWSQUARE LPAREN ss_expression COMA ss_expression COMA color RPAREN SEMICOLON'

def p_expression_drawcircle(p):
    'drawcircle : DRAWCIRCLE LPAREN ss_expression COMA ss_expression COMA color RPAREN SEMICOLON'

def p_expression_drawtriangle(p):
    'drawtriangle : DRAWTRIANGLE LPAREN ss_expression COMA ss_expression COMA color RPAREN SEMICOLON'

def p_expression_drawcurve(p):
    'drawcurve : DRAWCURVE LPAREN ss_expression COMA color RPAREN SEMICOLON'

def p_expression_drawpolygon(p):
    'drawpolygon : DRAWPOLYGON LPAREN ss_expression COMA ss_expression COMA color RPAREN SEMICOLON'

def p_expression_voidfunction(p):
    '''voidfunction : ID LPAREN call_params RPAREN SEMICOLON'''

def p_expression_functioncall(p):
    '''functioncall : ID LPAREN call_params RPAREN'''

def p_expression_call_params(p):
    '''call_params : ss_expression more_call_params
                   | empty'''

def p_expression_more_call_params(p):
    '''more_call_params : COMA ss_expression more_call_params
                        | empty'''

def p_expression_ciclo(p):
    '''ciclo : WHILE LPAREN ss_expression RPAREN bloque'''

def p_exxpression_lectura(p):
    'lectura : ID array ASSIGN INPUT SEMICOLON'

def p_expression_asignacion(p):
    'asignacion : ID array ASSIGN ss_expression SEMICOLON'

def p_expression_ss_expression(p):
    '''ss_expression : ss_not s_expression'''

def p_expression_ss_not(p):
    '''ss_not : NOT
              | empty'''

def p_expression_s_expression(p):
    's_expression : expresion s_and_or'

def p_expression_s_and_or(p):
    '''s_and_or : AND s_expression
                | OR s_expression
                | empty'''

def p_expression_expresion(p):
    'expresion : expr exp'

def p_expression_expr(p):
    'expr : termino term'

def p_expression_exp(p):
    '''exp : empty
          | GT expr
          | LT expr
          | GE expr
          | LE expr
          | EQUAL expr
          | DIFFERENT expr'''

def p_exppression_termino(p):
    'termino : factor fact'

def p_expression_term(p):
    '''term : PLUS termino term
        | MINUS termino term
        | empty'''

def p_expression_factor(p):
    '''factor : LPAREN ss_expression RPAREN
              | signo constante'''

def p_expression_fact(p):
    '''fact : TIMES factor fact
        | DIVISION factor fact
        | empty'''

def p_expression_signo(p):
    '''signo : PLUS
            | MINUS
            | empty'''

def p_expression_constante(p):
    '''constante : ID id_func_array
                 | CTEI
                 | CTEF
                 | CTES'''

def p_expression_id_func_array(p):
    '''id_func_array : LARRAY expr RARRAY
                     | LPAREN call_params RPAREN
                     | empty'''

def p_expression_escritura(p):
    'escritura : PRINT LPAREN ss_expression RPAREN SEMICOLON'

def p_expression_condicion(p):
    'condicion : IF LPAREN ss_expression RPAREN bloque else'

def p_expression_else(p):
    '''else : ELSE bloque
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

print(funcDir.functions)

for function in funcDir.functions:
    func = funcDir.functions[function]
    print(func)

# while True:
#    try:
#        s = raw_input()
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(code)
#    print(result)