from Memory.MainMemory import MainMemory
import sys


class LancerVM:
    def __init__(self):
        self.memory = MainMemory()
        self.instruction_stack = []
        self.execution_stack = []
        self.instruction_pointer = 0

    def printMainMemory(self):
        self.memory.printMemory()

    def setInitialInstructionPointer(self, startingPointer):
        self.instruction_pointer = startingPointer

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
