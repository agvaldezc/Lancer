#Alan Gustavo Valdez Cascajares A01336955
#Rafael Manriquez Valdez

import ply.yacc as yacc
import sys as sys
from LancerLex import tokens
from Directories.FunctionDirectory import FunctionDirectory
from Directories.Stack import Stack
from Semantic_Cubes.SemanticCubeDict import SemanticCubeDict
from Quadruples.Quadruple import Quadruple

funcDir = FunctionDirectory()
currentScope = ""
globalScope = ""
OperandStack = []
OperatorStack = []
TypeStack = []
semanticCube = SemanticCubeDict()
quadruples = []
tempCont = 0

ERROR_CODES = {'func_already_declared': -5, 'variable_already_declared': -6, 'func_not_declared': -7,
               'variable_not_declared': -8, 'type_mismatch': -9, 'syntax_error': -10}

#Reglas gramaticales expresadas en funciones
def p_expression_programa(p):
    'prog : PROGRAMA ID create_func_dir SEMICOLON vars function MAIN switch_global_scope bloque'
    print('Correct Syntax.')

def p_expression_switch_global_scope(p):
    'switch_global_scope : '

    global globalScope
    global currentScope

    currentScope = globalScope

def p_expression_create_func_dir(p):
    'create_func_dir : '

    #Save current function name (scope)
    global currentScope
    global globalScope

    globalScope = p[-1]
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
        print('Error: Variable already declared.')
        sys.exit(ERROR_CODES['variable_already_declared'])

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
        print('Error: Variable already declared.')
        sys.exit(ERROR_CODES['variable_already_declared'])

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
        print('Error: Function already declared.')
        sys.exit(ERROR_CODES['func_already_declared'])

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
    'lectura : ID push_id_operand array ASSIGN push_operator INPUT SEMICOLON'

def p_expression_asignacion(p):
    'asignacion : ID push_id_operand array ASSIGN push_operator ss_expression SEMICOLON'

def p_expression_ss_expression(p):
    '''ss_expression : ss_not s_expression'''

def p_expression_ss_not(p):
    '''ss_not : NOT push_operator
              | empty'''

def p_expression_s_expression(p):
    's_expression : expresion s_and_or'

def p_expression_s_and_or(p):
    '''s_and_or : AND push_operator s_expression
                | OR push_operator s_expression
                | empty'''

def p_expression_expresion(p):
    'expresion : expr exp'

def p_expression_expr(p):
    'expr : termino term'

def p_expression_exp(p):
    '''exp : empty
          | GT push_operator expr solve_pending_relational
          | LT push_operator expr solve_pending_relational
          | GE push_operator expr solve_pending_relational
          | LE push_operator expr solve_pending_relational
          | EQUAL push_operator expr solve_pending_relational
          | DIFFERENT push_operator expr solve_pending_relational'''

def p_expression_solve_pending_relational(p):
    'solve_pending_relational : '

    relOps = {'<', '>', '==', '>=', '<=', '<>'}

    if OperatorStack[len(OperatorStack) - 1] in relOps:
        solvePendingOperations(p)

def p_exppression_termino(p):
    'termino : factor fact'

def p_expression_term(p):
    '''term : PLUS push_operator termino solve_pending_term term
        | MINUS push_operator termino solve_pending_term term
        | empty'''

def p_expression_solve_pending_term(p):
    'solve_pending_term : '

    if OperatorStack[len(OperatorStack) - 1] == '+' or OperatorStack[len(OperatorStack) - 1] == '-':
        solvePendingOperations(p)

def p_expression_factor(p):
    '''factor : LPAREN create_false_bottom ss_expression RPAREN delete_false_bottom
              | signo constante'''

def p_expression_create_false_bottom(p):
    'create_false_bottom : '

    OperatorStack.append('(')

def p_expression_delete_false_bottom(p):
    'delete_false_bottom : '

    OperatorStack.pop()

def p_expression_fact(p):
    '''fact : TIMES push_operator factor solve_pending_factor fact
        | DIVISION push_operator factor solve_pending_factor fact
        | empty'''

def p_expression_solve_pending_factor(p):
    'solve_pending_factor : '

    if OperatorStack[len(OperatorStack) - 1] == '*' or OperatorStack[len(OperatorStack) - 1] == '/':
        solvePendingOperations(p)

def p_expression_signo(p):
    '''signo : PLUS push_operator
            | MINUS push_operator
            | empty'''

def p_expression_constante(p):
    '''constante : ID push_id_operand id_func_array
                 | CTEI push_int_operand
                 | CTEF push_float_operand
                 | CTES push_string_operand'''

def p_expression_id_func_array(p):
    '''id_func_array : LARRAY expr RARRAY
                     | LPAREN call_params RPAREN
                     | empty'''

def p_expression_push_id_operand(p):
    '''push_id_operand : '''

    global currentScope

    variable = funcDir.getVariable(currentScope, p[-1])

    if variable is None:
        variable = funcDir.getVariable(globalScope, p[-1])

        if variable is None:
            print('Error: variable {0} not declared in line {1}'.format(p[-1], p.lexer.lineno))
            sys.exit(-2)
        else:
            OperandStack.append(variable[0])
            TypeStack.append(variable[1])
            print(variable)
    else:
        OperandStack.append(variable[0])
        TypeStack.append(variable[1])
        print(variable)


def p_expression_push_int_operand(p):
    '''push_int_operand : '''

    global OperandStack
    global OperatorStack

    OperandStack.append(p[-1])
    TypeStack.append('int')

def p_expression_push_float_operand(p):
    '''push_float_operand : '''

    global OperandStack
    global OperatorStack

    OperandStack.append(p[-1])
    TypeStack.append('float')

def p_expression_push_string_operand(p):
    '''push_string_operand : '''

    global OperandStack
    global OperatorStack

    OperandStack.append(p[-1])
    TypeStack.append('string')

def p_expression_push_operator(p):
    'push_operator : '

    OperatorStack.append(p[-1])

def p_expression_escritura(p):
    'escritura : PRINT LPAREN ss_expression RPAREN SEMICOLON'

def p_expression_condicion(p):
    'condicion : IF LPAREN ss_expression RPAREN bloque else'

def p_expression_else(p):
    '''else : ELSE bloque
            | empty'''

#Error de sintaxis
def p_error(p):
    print('Syntax error in input in line {0}'.format(p.lexer.lineno))
    sys.exit(ERROR_CODES['syntax_error'])

#Definicion de espacio vacio
def p_empty(p):
    'empty :'
    pass

def solvePendingOperations(p):
    right_operand = OperandStack.pop()
    right_type = TypeStack.pop()
    left_operand = OperandStack.pop()
    left_type = TypeStack.pop()
    operator = OperatorStack.pop()

    global semanticCube
    global tempCont

    semanticResult = semanticCube.getSemanticType(left_type, right_type, operator)

    if semanticResult != 'error':
        quad = Quadruple(operator, left_operand, right_operand, tempCont)
        quadruples.append(quad)

        tempCont += 1

        #int
        if semanticResult == 0:
            OperandStack.append('1')
        #float
        if semanticResult == 1:
            OperandStack.append('1.0')
        #bool
        if semanticResult == 2:
            OperandStack.append('true')
        #string
        if semanticResult == 3:
            OperandStack.append('hello')

        TypeStack.append(semanticResult)
    else:
        print('ERROR: type mismatch in line {0}'.format(p.lexer.lineno))
        sys.exit(ERROR_CODES['type_mismatch'])


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
    print(func['variables'].variables)

print(OperandStack)
print(TypeStack)
print(OperatorStack)

for quad in quadruples:
    quad.printQuad()

print('current scope: {0}, global scope: {1}'.format(currentScope, globalScope))

# while True:
#    try:
#        s = raw_input()
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(code)
#    print(result)