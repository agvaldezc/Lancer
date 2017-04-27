from Memory.MainMemory import MainMemory
from Directories.FunctionDirectory import FunctionDirectory
import sys
from graphics import *


class LancerVM:
    def __init__(self):
        self.memory = MainMemory()
        self.instruction_stack = []
        self.instruction_pointer = 0
        self.funcDir = FunctionDirectory()
        self.execution_stack = []
        self.window_width = 640
        self.window_height = 480
        self.main_name = ""

    def printMainMemory(self):
        self.memory.printMemory()

    def isInt(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return False

    def isFloat(self, value):
        try:
            return float(value)
        except (ValueError, TypeError):
            return False

    def isBool(self, value):
        try:
            return bool(value)
        except (ValueError, TypeError):
            return False

    def isString(self, value):
        try:
            return str(value)
        except (ValueError, TypeError):
            return False

    def setMainName(self, mainName):
        self.main_name = mainName

    def setFuncDir(self, funcDir):
        self.funcDir = funcDir

    def setInitialInstructionPointer(self, startingPointer):
        self.instruction_pointer = startingPointer - 1

    def getInstructions(self, instruction_stack):
        self.instruction_stack = instruction_stack

    def printInstructions(self):
        for instruction in self.instruction_stack:
            instruction.printQuad()

    def executeInstructions(self):

        print("Started Execution")
        totalInstructions = len(self.instruction_stack)

        savedInstructionPointer = []

        window = GraphWin(self.main_name, self.window_width, self.window_height)

        while self.instruction_pointer < totalInstructions:
            instruction = self.instruction_stack[self.instruction_pointer]

            #print(instruction.printQuad())

            instructionCode = instruction.operator
            leftOperandVirtualAddress = instruction.left_operand
            rightOperandVirtualAddress = instruction.right_operand
            resultVirtualAddress = instruction.result

            if isinstance(leftOperandVirtualAddress, list):
                if len(leftOperandVirtualAddress) == 1:
                    leftOperandVirtualAddress = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress[0])
            if isinstance(rightOperandVirtualAddress, list):
                if len(rightOperandVirtualAddress) == 1:
                    rightOperandVirtualAddress = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress[0])
            if isinstance(resultVirtualAddress, list):
                if len(resultVirtualAddress) == 1:
                    resultVirtualAddress = self.memory.getValueFromVirtualAddress(resultVirtualAddress[0])


            if instructionCode == '+':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand + rightOperand))
                self.instruction_pointer += 1

            elif instructionCode == '-':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand - rightOperand))
                self.instruction_pointer += 1

            elif instructionCode == '*':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand * rightOperand))
                self.instruction_pointer += 1

            elif instructionCode == '/':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand / rightOperand))
                self.instruction_pointer += 1

            elif instructionCode == '=':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, leftOperand)
                self.instruction_pointer += 1

            elif instructionCode == 'print':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)

                print(leftOperand)
                self.instruction_pointer += 1
            elif instructionCode == '<':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand < rightOperand))
                self.instruction_pointer += 1
            elif instructionCode == '>':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand > rightOperand))
                self.instruction_pointer += 1
            elif instructionCode == '==':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand == rightOperand))
                self.instruction_pointer += 1
            elif instructionCode == '<>':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand != rightOperand))
                self.instruction_pointer += 1
            elif instructionCode == '<=':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand <= rightOperand))
                self.instruction_pointer += 1
            elif instructionCode == '>=':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand >= rightOperand))
                self.instruction_pointer += 1
            elif instructionCode == '&&':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand and rightOperand))
                self.instruction_pointer += 1
            elif instructionCode == '||':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand or rightOperand))
                self.instruction_pointer += 1
            elif instructionCode == 'GoToF':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                jumpPointer = resultVirtualAddress

                if leftOperand:
                    self.instruction_pointer += 1
                else:
                    self.instruction_pointer = jumpPointer - 1

            elif instructionCode == 'GoTo':
                jumpPointer = resultVirtualAddress
                self.instruction_pointer = jumpPointer - 1

            elif instructionCode == 'validate':
                index = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)

                inferiorLimit = rightOperandVirtualAddress
                superiorLimit = resultVirtualAddress

                if not (index >= inferiorLimit and index <= superiorLimit):
                    print("ERROR: Array index out of bounds. Index overflow.")
                    sys.exit(4)
                else:
                    self.instruction_pointer += 1

            elif instructionCode == 'RETURN':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, leftOperand)

                self.instruction_pointer += 1

            elif instructionCode == 'ERA':
                function = self.funcDir.functions[leftOperandVirtualAddress]

                varTable = function['variables']
                variables = varTable.variables

                # functionData = self.funcDir.getVariable(self.main_name, leftOperandVirtualAddress)
                # functionVirtualAddress = functionData[1][1]
                # functionValue =  self.memory.getValueFromVirtualAddress(functionVirtualAddress)
                #
                # backupMemoryState = [{functionVirtualAddress: functionValue}]

                backupMemoryState = []

                for variable in variables:
                    if variable != 'total' and variable != 'temp_total':
                        variableInfo = variables[variable]

                        variableVirtualAddress = variableInfo[1]
                        variableValue = self.memory.getValueFromVirtualAddress(variableVirtualAddress)

                        backupMemoryState.append({variableVirtualAddress: variableValue})

                self.execution_stack.append(backupMemoryState)
                self.instruction_pointer += 1

                #print(self.execution_stack)

            elif instructionCode == 'ENDPROC':
                backupMemoryState = self.execution_stack.pop()
                #print("backup state: {0}".format(backupMemoryState))
                print("execution stack: {0}".format(self.execution_stack))
                for state in backupMemoryState:
                    virtualAddress = state.keys()
                    virtualAddress = virtualAddress[0]
                    self.memory.editValueFromVirtualAddress(virtualAddress, state[virtualAddress])

                #print("saved IP: {0}". format(savedInstructionPointer))
                self.instruction_pointer = savedInstructionPointer.pop() + 1

            elif instructionCode == 'Parameter':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, leftOperand)

                self.instruction_pointer += 1

            elif instructionCode == 'GoSub':
                savedInstructionPointer.append(self.instruction_pointer)
                self.instruction_pointer = resultVirtualAddress - 1
            elif instructionCode == 'DRAWLINE':

                values = []

                for numberAddress in leftOperandVirtualAddress:
                    if isinstance(numberAddress, list):
                        numberAddress = self.memory.getValueFromVirtualAddress(numberAddress[0])
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)
                    else:
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)

                line = Line(Point(values[0], values[1]), Point(values[2], values[3]))

                line.setFill(rightOperandVirtualAddress)
                line.setWidth(2)
                line.draw(window)

                self.instruction_pointer += 1
            elif instructionCode == 'DRAWCIRCLE':

                values = []

                for numberAddress in leftOperandVirtualAddress:
                    if isinstance(numberAddress, list):
                        numberAddress = self.memory.getValueFromVirtualAddress(numberAddress[0])
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)
                    else:
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)

                line = Circle(Point(values[0], values[1]), values[2])

                line.setFill(rightOperandVirtualAddress)
                line.setWidth(2)
                line.draw(window)

                self.instruction_pointer += 1
            elif instructionCode == 'DRAWOVAL':

                values = []

                for numberAddress in leftOperandVirtualAddress:
                    if isinstance(numberAddress, list):
                        numberAddress = self.memory.getValueFromVirtualAddress(numberAddress[0])
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)
                    else:
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)

                line = Oval(Point(values[0], values[1]), Point(values[2], values[3]))

                line.setFill(rightOperandVirtualAddress)
                line.setWidth(2)
                line.draw(window)

                self.instruction_pointer += 1
            elif instructionCode == 'DRAWRECTANGLE':

                values = []

                for numberAddress in leftOperandVirtualAddress:
                    if isinstance(numberAddress, list):
                        numberAddress = self.memory.getValueFromVirtualAddress(numberAddress[0])
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)
                    else:
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)

                line = Rectangle(Point(values[0], values[1]), Point(values[2], values[3]))

                line.setFill(rightOperandVirtualAddress)
                line.setWidth(2)
                line.draw(window)

                self.instruction_pointer += 1
            elif instructionCode == 'DRAWTRIANGLE':

                values = []

                for numberAddress in leftOperandVirtualAddress:
                    if isinstance(numberAddress, list):
                        numberAddress = self.memory.getValueFromVirtualAddress(numberAddress[0])
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)
                    else:
                        value = self.memory.getValueFromVirtualAddress(numberAddress)

                        values.append(value)

                line = Polygon(Point(values[0], values[1]), Point(values[2], values[3]), Point(values[4], values[5]))

                line.setFill(rightOperandVirtualAddress)
                line.setWidth(2)
                line.draw(window)

                self.instruction_pointer += 1

            elif instructionCode == 'input':

                value = raw_input()

                if self.isInt(value):
                    if leftOperandVirtualAddress == 'int':
                        self.memory.editValueFromVirtualAddress(resultVirtualAddress, int(value))
                    else:
                        print('Error: Input type mismatch, expected {0} and got int'.format(leftOperandVirtualAddress))
                        sys.exit(15)
                elif self.isFloat(value):
                    if leftOperandVirtualAddress == 'float':
                        self.memory.editValueFromVirtualAddress(resultVirtualAddress, float(value))
                    else:
                        print('Error: Input type mismatch, expected {0} and got float'.format(leftOperandVirtualAddress))
                        sys.exit(15)
                elif value == 'true' or value == 'false':
                    if leftOperandVirtualAddress == 'bool':
                        self.memory.editValueFromVirtualAddress(resultVirtualAddress, bool(value))
                    else:
                        print('Error: Input type mismatch, expected {0} and got bool'.format(leftOperandVirtualAddress))
                        sys.exit(15)
                else:
                    if leftOperandVirtualAddress == 'string':
                        self.memory.editValueFromVirtualAddress(resultVirtualAddress, str(value))
                    else:
                        print('Error: Input type mismatch, expected {0} and got string'.format(leftOperandVirtualAddress))
                        sys.exit(15)


                self.instruction_pointer += 1

            #End of while

        window.getMouse()