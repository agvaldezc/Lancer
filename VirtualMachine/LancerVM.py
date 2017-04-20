from Memory.MainMemory import MainMemory
from Directories.FunctionDirectory import FunctionDirectory
import sys


class LancerVM:
    def __init__(self):
        self.memory = MainMemory()
        self.instruction_stack = []
        self.execution_stack = []
        self.instruction_pointer = 0
        self.funcDir = FunctionDirectory()
        self.execution_stack = []

    def printMainMemory(self):
        self.memory.printMemory()

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

        savedInstructionPointer = self.instruction_pointer

        while self.instruction_pointer < totalInstructions:
            instruction = self.instruction_stack[self.instruction_pointer]
            #print(instruction.printQuad())
            instructionCode = instruction.operator
            leftOperandVirtualAddress = instruction.left_operand
            rightOperandVirtualAddress = instruction.right_operand
            resultVirtualAddress = instruction.result

            if isinstance(leftOperandVirtualAddress, list):
                leftOperandVirtualAddress = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress[0])
            if isinstance(rightOperandVirtualAddress, list):
                rightOperandVirtualAddress = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress[0])
            if isinstance(resultVirtualAddress, list):
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

                backupMemoryState = []

                for variable in variables:
                    if variable != 'total' and variable != 'temp_total':
                        variableInfo = variables[variable]

                        variableVirtualAddress = variableInfo[1]
                        variableValue = self.memory.getValueFromVirtualAddress(variableVirtualAddress)

                        backupMemoryState.append({variableVirtualAddress: variableValue})

                self.execution_stack.append(backupMemoryState)
                self.instruction_pointer += 1

            elif instructionCode == 'ENDPROC':
                backupMemoryState = self.execution_stack.pop()

                for state in backupMemoryState:
                    virtualAddress = state.keys()
                    virtualAddress = virtualAddress[0]
                    self.memory.editValueFromVirtualAddress(virtualAddress, state[virtualAddress])

                self.instruction_pointer = savedInstructionPointer + 1

            elif instructionCode == 'Parameter':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, leftOperand)

                self.instruction_pointer += 1

            elif instructionCode == 'GoSub':
                savedInstructionPointer = self.instruction_pointer
                self.instruction_pointer = resultVirtualAddress - 1