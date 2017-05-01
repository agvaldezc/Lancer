# Alan Gustavo Valdez Cascajares A01336955
# Rafael Manriquez Valdez

import ply.yacc as yacc
import sys

sys.path.append("../../Lancer")

# Clases definidas por nosotros
from LancerLex import tokens
from Directories.FunctionDirectory import FunctionDirectory
from Directories.Stack import Stack
from Semantic_Cubes.SemanticCubeDict import SemanticCubeDict
from Quadruples.Quadruple import Quadruple
from VirtualMachine.LancerVM import LancerVM
from Memory.MainMemory import MainMemory

# Variables globales a utilizar
funcDir = FunctionDirectory()
currentScope = ""
globalScope = ""
OperandStack = []
OperatorStack = []
TypeStack = []
JumpStack = []
ReturnStack = []
semanticCube = SemanticCubeDict()
quadruples = []
tempCont = 0
quadCont = 1
FunctionToCall = ""
ArgumentNumber = 0
ArgumentStack = []
ArgumentTypeStack = []
VM = LancerVM()
dimensionVariableName = ""
dimension = {}
hasReturnStatement = False
drawParameters = []
drawColor = ""

trashValues = {'int': 1, 'float': 1.0, 'bool': True, 'string': 'Null'}

ERROR_CODES = {'func_already_declared': -5, 'variable_already_declared': -6, 'func_not_declared': -7,
               'variable_not_declared': -8, 'type_mismatch': -9, 'syntax_error': -10, 'parameter_type_mismatch': -11,
               'memory_error': 3, 'no_return_statement': 4, 'return_type_mismatch': 5}


# Reglas gramaticales expresadas en funciones
def p_expression_programa(p):
    'prog : PROGRAMA ID create_func_dir SEMICOLON vars function MAIN switch_global_scope bloque'
    print('Correct Syntax.')


def p_expression_switch_global_scope(p):
    'switch_global_scope : '

    global globalScope
    global currentScope

    currentScope = globalScope
    funcDir.fillStartingQuad(globalScope, quadCont)

def p_expression_create_func_dir(p):
    'create_func_dir : '

    # Save current function name (scope)
    global currentScope
    global globalScope

    globalScope = p[-1]
    currentScope = p[-1]

    # Create function directory variable
    funcDir.addFunction(currentScope, 'void')


def p_expression_vars(p):
    '''vars : VAR ID array_declaration COLON type add_var SEMICOLON vars
            | empty'''


def p_expression_add_var(p):
    'add_var : '

    global currentScope
    global dimensionVariableName
    global dimension

    varName = p[-4]
    varType = p[-1]

    if currentScope == globalScope:
        if dimensionVariableName != "":
            virtualAddress = VM.memory.addDimensionGlobalValue(dimension['superior'], trashValues[varType], varType)
        else:
            virtualAddress = VM.memory.addGlobalValue(trashValues[varType], varType)

    else:
        if dimensionVariableName != "":
            virtualAddress = VM.memory.addDimenionTempValue(dimension['superior'], trashValues[varType], varType)
        else:
            virtualAddress = VM.memory.addTempValue(trashValues[varType], varType)

    if virtualAddress == None:
        print('ERROR: Impossible memory allocation, out of memory.')
        sys.exit(ERROR_CODES['memory_error'])

    if not funcDir.addFunctionVariable(currentScope, varName, varType, virtualAddress):
        print('Error: Variable already declared.')
        sys.exit(ERROR_CODES['variable_already_declared'])

    if dimensionVariableName != "":
        funcDir.addDimensionToVariable(currentScope, varName, dimension)
        dimensionVariableName = ""
        dimension = {}



def p_expression_array_declaration(p):
    '''array_declaration : LARRAY identify_dimensional_var ss_expression create_dimension RARRAY
                         | empty'''


def p_expression_identify_dimensional_var(p):
    'identify_dimensional_var : '

    global dimensionVariableName

    dimensionVariableName = p[-2]

def p_expression_create_dimension(p):
    'create_dimension : '

    global dimension

    indexVirtualAddress = OperandStack.pop()
    indexType = TypeStack.pop()

    if indexType != 'int':
        print('ERROR: Expected int index type, found {0} in line {1}'.format(indexType, p.lexer.lineno))
        sys.exit(ERROR_CODES['parameter_type_mismatch'])
    else:
        dimensionSize = VM.memory.getValueFromVirtualAddress(indexVirtualAddress)
        dimension = {'inferior': 0, 'superior': dimensionSize - 1}


def p_expression_type(p):
    '''type : INT_TYPE
            | FLOAT_TYPE
            | STRING_TYPE
            | BOOL_TYPE'''
    p[0] = p[1]


def p_expression_array(p):
    '''array : LARRAY identify_dimension ss_expression validate_array_bounds_quad RARRAY
             | empty'''


def p_expression_function(p):
    '''function : FUNC func_type ID add_to_func_dir LPAREN parameters RPAREN vars starting_quad bloque end_proc function
                | empty'''


def p_expression_end_proc(p):
    'end_proc : '
    global quadCont
    global ReturnStack

    functionType = funcDir.getFunctionType(currentScope)

    if functionType != 'void':
        if not hasReturnStatement:
            print('Error: Function {0} of type {1} has no return statement.'.format(currentScope, functionType))
            sys.exit(ERROR_CODES['no_return_statement'])
        else:
            quad = Quadruple(quadCont, 'ENDPROC', None, None, None)
            quadruples.append(quad)

            for i in ReturnStack:
                quadruples[i - 1].fillJumpQuad(quadCont)

            ReturnStack = []

            quadCont += 1
    else:
        quad = Quadruple(quadCont, 'ENDPROC', None, None, None)
        quadruples.append(quad)

        ReturnStack = []

        quadCont += 1

def p_expression_starting_quad(p):
    'starting_quad : '
    funcDir.fillStartingQuad(currentScope, quadCont)


def p_expression_func_type(p):
    '''func_type : VOID
                 | type'''
    p[0] = p[1]


def p_expression_add_to_func_dir(p):
    'add_to_func_dir : '

    global currentScope

    funcName = p[-1]
    funcType = p[-2]

    if not funcType == 'void':
        virtualAddress = VM.memory.addGlobalValue(trashValues[funcType], funcType)
        funcDir.addFunctionVariable(globalScope, funcName, funcType, virtualAddress)

    if not funcDir.functionExists(funcName):
        currentScope = funcName
        funcDir.addFunction(funcName, funcType)
    else:
        print('Error: Function already declared in line {0}.'.format(p.lexer.lineno))
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

    if currentScope == globalScope:
        virtualAddress = VM.memory.addGlobalValue(trashValues[paramType], paramType)
    else:
        virtualAddress = VM.memory.addTempValue(trashValues[paramType], paramType)

    if funcDir.addFunctionVariable(currentScope, paramName, paramType, virtualAddress):
        funcDir.addParameterTypes(currentScope, [paramType])
        funcDir.addParameterAddress(currentScope, [virtualAddress])


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

    global hasReturnStatement
    global quadCont

    hasReturnStatement = True

    leftOperand = OperandStack.pop()
    leftOperandType = TypeStack.pop()

    functionType = funcDir.getFunctionType(currentScope)
    functionVariable = funcDir.getVariable(globalScope, currentScope)
    functionProperties = functionVariable[1][1]

    if leftOperandType != functionType:
        print("Return statement is trying to return {0} and function return type is {1}.".format(leftOperandType, functionType))
        sys.exit()

    quad = Quadruple(quadCont, 'RETURN', leftOperand, None, functionProperties)
    quadruples.append(quad)

    quadCont += 1

    quad = Quadruple(quadCont, 'GoTo', None, None, None)
    quadruples.append(quad)

    ReturnStack.append(quadCont)

    quadCont += 1

def p_expression_predefined(p):
    '''predefined : drawcircle
                  | drawrectangle
                  | drawtriangle
                  | drawline
                  | drawoval'''


def p_expression_color(p):
    '''color : RED
             | GREEN
             | BLUE
             | YELLOW
             | BROWN
             | BLACK'''
    p[0] = p[1]

def p_expression_drawline(p):
    'drawline : DRAWLINE LPAREN ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA color collect_draw_color RPAREN SEMICOLON'

    global quadCont
    global drawColor
    global drawParameters

    quad = Quadruple(quadCont, 'DRAWLINE', drawParameters, drawColor, None)
    quadruples.append(quad)

    quadCont += 1

    drawColor = ""
    drawParameters = []

def p_expression_collect_draw_argument(p):
    'collect_draw_argument : '

    operand = OperandStack.pop()
    operandType = TypeStack.pop()

    if operandType != 'int' and operandType != 'float':
        print('Error: Argument type mismatch. Expected float or int, got {0} in line {1}'.format(operandType, p.lexer.lineno))
        sys.exit(ERROR_CODES['parameter_type_mismatch'])
    else:
        drawParameters.append(operand)

def p_expression_collect_draw_color(p):
    'collect_draw_color : '

    global drawColor

    drawColor = p[-1]

def p_expression_drawrectangle(p):
    '''drawrectangle : DRAWRECTANGLE LPAREN ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA color collect_draw_color RPAREN SEMICOLON'''

    global quadCont
    global drawColor
    global drawParameters

    quad = Quadruple(quadCont, 'DRAWRECTANGLE', drawParameters, drawColor, None)
    quadruples.append(quad)

    quadCont += 1

    drawColor = ""
    drawParameters = []


def p_expression_drawcircle(p):
    'drawcircle : DRAWCIRCLE LPAREN ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA color collect_draw_color RPAREN SEMICOLON'

    global quadCont
    global drawColor
    global drawParameters

    quad = Quadruple(quadCont, 'DRAWCIRCLE', drawParameters, drawColor, None)
    quadruples.append(quad)

    quadCont += 1

    drawColor = ""
    drawParameters = []


def p_expression_drawtriangle(p):
    'drawtriangle : DRAWTRIANGLE LPAREN ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA color collect_draw_color RPAREN SEMICOLON'

    global quadCont
    global drawColor
    global drawParameters

    quad = Quadruple(quadCont, 'DRAWTRIANGLE', drawParameters, drawColor, None)
    quadruples.append(quad)

    quadCont += 1

    drawColor = ""
    drawParameters = []


def p_expression_drawoval(p):
    'drawoval : DRAWOVAL LPAREN ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA ss_expression collect_draw_argument COMA color collect_draw_color RPAREN SEMICOLON'

    global quadCont
    global drawColor
    global drawParameters

    quad = Quadruple(quadCont, 'DRAWOVAL', drawParameters, drawColor, None)
    quadruples.append(quad)

    quadCont += 1

    drawColor = ""
    drawParameters = []

def p_expression_voidfunction(p):
    '''voidfunction : ID validate_function_id LPAREN generate_era call_params RPAREN SEMICOLON argument_validation'''


def p_expression_functioncall(p):
    '''functioncall : ID validate_function_id LPAREN generate_era call_params RPAREN argument_validation'''


def p_expression_argument_validation(p):
    'argument_validation : '

    global quadCont
    global ArgumentNumber
    global ArgumentStack
    global ArgumentTypeStack
    global FunctionToCall

    if FunctionToCall == "":
        virtualAddress = OperandStack.pop()
        FunctionToCall = funcDir.getFunctionIdByAddress(globalScope, virtualAddress)

    functionParameterAddresses = funcDir.getParameterAddresses(FunctionToCall)

    if funcDir.validateParameters(FunctionToCall, ArgumentTypeStack):
        for argument in ArgumentStack:
            quad = Quadruple(quadCont, 'Parameter', argument, None, functionParameterAddresses[ArgumentNumber])
            quadruples.append(quad)

            quadCont += 1
            ArgumentNumber += 1

        quad = Quadruple(quadCont, 'GoSub', FunctionToCall, None, funcDir.getFunctionStartingQuad(FunctionToCall))
        quadruples.append(quad)

        quadCont += 1

        functionType = funcDir.getFunctionType(FunctionToCall)

        if functionType != 'void':
            funcDir.addTempVariable(globalScope, functionType)
            virtualAddress = VM.memory.addTempValue(trashValues[functionType], functionType)

            functionVariable = funcDir.getVariable(globalScope, FunctionToCall)

            quad = Quadruple(quadCont, '=', functionVariable[1][1], None, virtualAddress)
            quadruples.append(quad)

            quadCont += 1

            OperandStack.append(virtualAddress)

        ArgumentStack = []
        ArgumentTypeStack = []
        FunctionToCall = ""
        ArgumentNumber = 0
    else:
        print('Error: argument type mismatch in line {0} using function {1}.'.format(p.lexer.lineno, FunctionToCall))
        sys.exit(ERROR_CODES['parameter_type_mismatch'])


def p_expression_generate_era(p):
    'generate_era : '

    global quadCont

    function = p[-3]

    quad = Quadruple(quadCont, 'ERA', function, None, None)
    quadruples. append(quad)

    quadCont += 1


def p_expression_validate_function_id(p):
    'validate_function_id : '

    global FunctionToCall
    FunctionToCall = p[-1]

    if not funcDir.functionExists(FunctionToCall):
        print('Error: function {0} not declared in line {1}'.format(FunctionToCall, p.lexer.lineno))
        sys.exit(ERROR_CODES['func_not_declared'])


def p_expression_call_params(p):
    '''call_params : ss_expression function_argument_collection more_call_params
                   | empty'''


def p_expression_more_call_params(p):
    '''more_call_params : COMA ss_expression function_argument_collection more_call_params
                        | empty'''


def p_expression_function_argument_collection(p):
    'function_argument_collection : '
    functionArgumentCollection(p)


def p_expression_ciclo(p):
    '''ciclo : WHILE create_while_quad LPAREN ss_expression RPAREN while_expression_evaluation bloque while_end'''


def p_expression_create_while_quad(p):
    'create_while_quad : '
    whileConditionQuads(p)


def p_expression_while_expression_evaluation(p):
    'while_expression_evaluation : '
    whileEvaluationQuad(p)


def p_expression_while_end(p):
    'while_end : '
    whileEndQuad(p)


def p_expression_lectura(p):
    'lectura : ID push_id_operand array ASSIGN push_operator INPUT SEMICOLON'
    inputAssignment(p)


def p_expression_asignacion(p):
    'asignacion : ID push_id_operand array ASSIGN push_operator ss_expression SEMICOLON'
    assignQuad(p)


def p_expression_ss_expression(p):
    '''ss_expression : ss_not s_expression solve_not_operation'''


def p_expression_ss_not(p):
    '''ss_not : NOT push_operator
              | empty'''

def p_expression_solve_not_operation(p):
    'solve_not_operation : '

    if len(OperatorStack) > 0:
        if OperatorStack[len(OperatorStack) - 1] == '!!':
            solveNotOperation(p)

def p_expression_s_expression(p):
    's_expression : expresion s_and_or'

def p_expression_s_and_or(p):
    '''s_and_or : AND push_operator s_expression solve_pending_andor
                | OR push_operator s_expression solve_pending_andor
                | empty'''

def p_expression_solve_pending_andor(p):
    'solve_pending_andor : '

    andor = {'&&', '||'}

    if OperatorStack[len(OperatorStack) - 1] in andor:
        solvePendingOperations(p)

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
              | constante'''

#
# def p_expression_solve_negatives(p):
#     'solve_negatives : '
#
#     global quadCont
#
#     if len(OperatorStack) > 0:
#         if OperatorStack[len(OperatorStack) - 1] == '-' and len(OperandStack) > 2:
#             rightOperand = OperandStack.pop()
#             rightType = TypeStack.pop()
#             operator = OperatorStack.pop()
#
#             if rightType == 'int' or rightType == 'float':
#
#                 quad = Quadruple(quadCont, 'negative', 0, rightOperand, rightOperand)
#                 quadruples.append(quad)
#
#                 quadCont += 1
#
#                 OperandStack.append(rightOperand)
#                 TypeStack.append(rightType)

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


# def p_expression_signo(p):
#     '''signo : MINUS push_operator
#              | empty'''


def p_expression_constante(p):
    '''constante : ID push_id_operand id_func_array
                 | CTEI push_int_operand
                 | CTEF push_float_operand
                 | CTES push_string_operand
                 | cteb push_bool_operand'''

def p_expression_cteb(p):
    '''cteb : TRUE
            | FALSE'''
    p[0] = p[1]


def p_expression_id_func_array(p):
    '''id_func_array : LARRAY identify_dimension ss_expression validate_array_bounds_quad RARRAY
                     | LPAREN generate_era call_params RPAREN argument_validation
                     | empty'''

def p_expression_identify_dimension(p):
    'identify_dimension : '

    global dimension

    varName = p[-3]

    dimension = funcDir.getDimensions(currentScope, varName)

    dimension = dimension['dimensions']

    #print(dimension)

def p_expression_validate_array_bounds_quad(p):
    'validate_array_bounds_quad : '

    global quadCont

    indexVirtualAddress = OperandStack.pop()
    indexType = TypeStack.pop()

    if indexType != 'int':
        print('ERROR: Expected int index type, found {0} in line {1}'.format(indexType, p.lexer.lineno))
        sys.exit(ERROR_CODES['parameter_type_mismatch'])
    else:
        quad = Quadruple(quadCont, 'validate', indexVirtualAddress, dimension[1]['inferior'], dimension[1]['superior'])
        quadruples.append(quad)

        quadCont += 1

        arrayBaseAddress = OperandStack.pop()
        arrayType = TypeStack.pop()

        operationalBaseAddress = VM.memory.addTempValue(arrayBaseAddress, 'int')
        tempVirtualAddress = VM.memory.addTempValue(arrayBaseAddress, arrayType)

        quad = Quadruple(quadCont, '+', operationalBaseAddress, indexVirtualAddress, tempVirtualAddress)
        quadruples.append(quad)

        quadCont += 1

        OperandStack.append([tempVirtualAddress])
        TypeStack.append(arrayType)

def p_expression_push_id_operand(p):
    '''push_id_operand : '''

    global currentScope

    variable = funcDir.getVariable(currentScope, p[-1])

    if variable is None:
        variable = funcDir.getVariable(globalScope, p[-1])

        if variable is None:
            print('Error: variable {0} not declared in line {1}'.format(p[-1], p.lexer.lineno))
            sys.exit(ERROR_CODES['variable_not_declared'])
        else:
            variableInfo = variable[1]

            OperandStack.append(variableInfo[1])
            TypeStack.append(variableInfo[0])
    else:
        variableInfo = variable[1]

        OperandStack.append(variableInfo[1])
        TypeStack.append(variableInfo[0])


def p_expression_push_int_operand(p):
    '''push_int_operand : '''

    global OperandStack
    global OperatorStack

    virtualAddress = VM.memory.addConstantValue(int(p[-1]), 'int')

    OperandStack.append(virtualAddress)
    TypeStack.append('int')


def p_expression_push_float_operand(p):
    '''push_float_operand : '''

    global OperandStack
    global OperatorStack

    virtualAddress = VM.memory.addConstantValue(float(p[-1]), 'float')

    OperandStack.append(virtualAddress)
    TypeStack.append('float')


def p_expression_push_string_operand(p):
    '''push_string_operand : '''

    global OperandStack
    global OperatorStack

    oldString = p[-1]
    newString = oldString[1:-1]

    virtualAddress = VM.memory.addConstantValue(newString, 'string')

    OperandStack.append(virtualAddress)
    TypeStack.append('string')


def p_expression_push_bool_operand(p):
    'push_bool_operand : '

    global OperandStack
    global OperatorStack

    if p[-1] == "true":
        virtualAddress = VM.memory.addConstantValue(True, 'bool')
    else:
        virtualAddress = VM.memory.addConstantValue(False, 'bool')

    OperandStack.append(virtualAddress)
    TypeStack.append('bool')


def p_expression_push_operator(p):
    'push_operator : '

    OperatorStack.append(p[-1])


def p_expression_escritura(p):
    'escritura : PRINT LPAREN ss_expression RPAREN SEMICOLON'

    global quadCont

    printParameter = OperandStack.pop()
    printParameterType = TypeStack.pop()

    quad = Quadruple(quadCont, 'print', printParameter, None, None)
    quadruples.append(quad)
    quadCont += 1


def p_expression_condicion(p):
    'condicion : IF LPAREN ss_expression RPAREN create_condition_quad bloque else'
    endConditionQuads(p)


def p_expression_create_condition_quad(p):
    'create_condition_quad : '
    conditionQuads(p)


def p_expression_else(p):
    '''else : ELSE else_condition_quad bloque
            | empty'''


def p_expression_else_condition_quad(p):
    'else_condition_quad : '
    elseConditionQuad(p)


# Error de sintaxis
def p_error(p):
    print('Syntax error in input in line {0}'.format(p.lexer.lineno))
    sys.exit(ERROR_CODES['syntax_error'])


# Definicion de espacio vacio
def p_empty(p):
    'empty :'
    pass


def solvePendingOperations(p):
    right_operand = OperandStack.pop()
    right_type = TypeStack.pop()
    left_operand = OperandStack.pop()
    left_type = TypeStack.pop()
    operator = OperatorStack.pop()
    tempVarString = "t"

    global semanticCube
    global tempCont
    global quadCont

    semanticResult = semanticCube.getSemanticType(left_type, right_type, operator)

    if semanticResult != 'error':

        virtualTempAddress = VM.memory.addTempValue(trashValues[semanticResult], semanticResult)

        funcDir.addTempVariable(currentScope, semanticResult)
        # tempVarString = tempVarString + str(tempCont)
        quad = Quadruple(quadCont, operator, left_operand, right_operand, virtualTempAddress)
        quadruples.append(quad)

        quadCont += 1
        # tempCont += 1

        OperandStack.append(virtualTempAddress)

        TypeStack.append(semanticResult)
    else:
        print('ERROR: operation type mismatch in line {0}'.format(p.lexer.lineno))
        sys.exit(ERROR_CODES['type_mismatch'])


def assignQuad(p):
    right_operand = OperandStack.pop()
    right_type = TypeStack.pop()
    left_operand = OperandStack.pop()
    left_type = TypeStack.pop()
    operator = OperatorStack.pop()

    global semanticCube
    global tempCont
    global quadCont

    semanticResult = semanticCube.getSemanticType(left_type, right_type, operator)

    #print("{0} {1} {2} = {3}".format(left_type, operator, right_type, semanticResult))
    if semanticResult != 'error':
        quad = Quadruple(quadCont, operator, right_operand, None, left_operand)
        quadruples.append(quad)

        quadCont += 1
    else:
        print('ERROR: assignment type mismatch in line {0}'.format(p.lexer.lineno))
        sys.exit(ERROR_CODES['type_mismatch'])

def solveNotOperation(p):

    right_operand = OperandStack.pop()
    right_type = TypeStack.pop()
    operator = OperatorStack.pop()

    global semanticCube
    global tempCont
    global quadCont

    if right_type == 'bool':
        semanticResult = 'bool'
    else:
        semanticResult = 'error'

    if semanticResult != 'error':
        virtualTempAddress = VM.memory.addTempValue(trashValues[semanticResult], semanticResult)

        quad = Quadruple(quadCont, operator, right_operand, None, virtualTempAddress)
        quadruples.append(quad)

        OperandStack.append(virtualTempAddress)
        TypeStack.append(semanticResult)

        quadCont += 1
    else:
        print('ERROR: assignment type mismatch in line {0}'.format(p.lexer.lineno))
        sys.exit(ERROR_CODES['type_mismatch'])


def inputAssignment(p):
    global tempCont
    global quadCont

    right_operand = OperandStack.pop()
    right_type = TypeStack.pop()
    operator = OperatorStack.pop()

    inputQuad = Quadruple(quadCont, 'input', right_type, None, right_operand)
    quadruples.append(inputQuad)

    quadCont += 1

def conditionQuads(p):
    expressionType = TypeStack.pop()

    if expressionType != 'bool':
        print('ERROR: operation type mismatch in line {0}'.format(p.lexer.lineno))
        sys.exit(ERROR_CODES['type_mismatch'])
    else:
        global quadCont

        expressionResult = OperandStack.pop()
        quad = Quadruple(quadCont, 'GoToF', expressionResult, None, None)
        quadruples.append(quad)

        JumpStack.append(quadCont - 1)
        quadCont += 1


def elseConditionQuad(p):
    global quadCont

    quad = Quadruple(quadCont, 'GoTo', None, None, None)
    quadruples.append(quad)

    false = JumpStack.pop()

    JumpStack.append(quadCont - 1)
    quadCont += 1

    quad = quadruples[false]

    quad.fillJumpQuad(quadCont)


def endConditionQuads(p):
    end = JumpStack.pop()
    quad = quadruples[end]

    quad.fillJumpQuad(quadCont)


def whileConditionQuads(p):
    JumpStack.append(quadCont)


def whileEvaluationQuad(p):
    expressionType = TypeStack.pop()

    if expressionType != 'bool':
        print('ERROR: operation type mismatch in line {0}'.format(p.lexer.lineno))
        sys.exit(ERROR_CODES['type_mismatch'])
    else:
        global quadCont

        expressionResult = OperandStack.pop()
        quad = Quadruple(quadCont, 'GoToF', expressionResult, None, None)
        quadruples.append(quad)

        JumpStack.append(quadCont - 1)
        quadCont += 1


def whileEndQuad(p):
    end = JumpStack.pop()
    ret = JumpStack.pop()

    global quadCont

    endQuad = quadruples[end]
    quad = Quadruple(quadCont, 'GoTo', None, None, ret)

    quadCont += 1

    quadruples.append(quad)

    endQuad.fillJumpQuad(quadCont)


def functionArgumentCollection(p):
    argument = OperandStack.pop()
    argumentType = TypeStack.pop()

    ArgumentStack.append(argument)
    ArgumentTypeStack.append(argumentType)


def initParser():
    # Construir el parser
    parser = yacc.yacc(debug=1)

    # Escribir el nombre o ruta del archivo a leer
    print("Nombre o ruta del archivo a analizar: ")
    fileName = raw_input()

    # Abrir archivo
    file = open(fileName, 'r')
    code = file.read()

    # Parsear el codigo leido del archivo
    parser.parse(code)

    # print(funcDir.functions)

    #for function in funcDir.functions:
    #    func = funcDir.functions[function]
    #    print('{0} = {1}'.format(function, func))
    #    print(func['variables'].variables)

    print('Operand stack: {0}'.format(OperandStack))
    print('Type stack: {0}'.format(TypeStack))
    print('Operator stack: {0}'.format(OperatorStack))
    print('Jump stack: {0}'.format(JumpStack))

    VM.getInstructions(quadruples)
    VM.setFuncDir(funcDir)
    VM.setMainName(globalScope)
    VM.setInitialInstructionPointer(funcDir.getFunctionStartingQuad(globalScope))
    VM.printInstructions()
    VM.executeInstructions()
#    VM.printMainMemory()

initParser()
