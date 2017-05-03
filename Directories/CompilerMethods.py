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
        tempVarString = tempVarString + str(tempCont)
        quad = Quadruple(quadCont, operator, left_operand, right_operand, tempVarString)
        quadruples.append(quad)

        quadCont += 1
        tempCont += 1

        OperandStack.append(tempVarString)

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

    if semanticResult != 'error':
        quad = Quadruple(quadCont, operator, right_operand, None, left_operand)
        quadruples.append(quad)

        quadCont += 1
    else:
        print('ERROR: assignment type mismatch in line {0}'.format(p.lexer.lineno))
        sys.exit(ERROR_CODES['type_mismatch'])

def inputAssignment(p):
    global tempCont
    global quadCont

    tempVar = 't' + str(tempCont)

    inputQuad = Quadruple(quadCont, 'input', None, None, tempVar)
    quadruples.append(inputQuad)

    quadCont += 1

    OperandStack.append(tempVar)
    TypeStack.append('InputType')

    right_operand = OperandStack.pop()
    right_type = TypeStack.pop()
    left_operand = OperandStack.pop()
    left_type = TypeStack.pop()
    operator = OperatorStack.pop()

    tempCont = tempCont + 1

    assignInputQuad = Quadruple(quadCont, operator, right_operand, None, left_operand)
    quadruples.append(assignInputQuad)

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

    endQuad = quadruples[end]
    quad = Quadruple(quadCont, 'GoTo', None, None, ret)

    quadruples.append(quad)

    endQuad.fillJumpQuad(quadCont)