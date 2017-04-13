from Memory.MainMemory import MainMemory


class LancerVM:
    def __init__(self):
        self.memory = MainMemory()
        self.instruction_stack = []

    def printMainMemory(self):
        self.memory.printMemory()

    def getInstructions(self, instruction_stack):
        self.instruction_stack = instruction_stack

    def printInstructions(self):
        for instruction in self.instruction_stack:
            instruction.printQuad()

    def executeInstructions(self):

        print("Started Execution")
        totalInstructions = len(self.instruction_stack)

        instructionPointer = 0
        savedInstructionPointer = instructionPointer

        while instructionPointer < totalInstructions:
            instruction = self.instruction_stack[instructionPointer]

            instructionCode = instruction.operator
            leftOperandVirtualAddress = instruction.left_operand
            rightOperandVirtualAddress = instruction.right_operand
            resultVirtualAddress = instruction.result

            if instructionCode == '+':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand + rightOperand))
                instructionPointer += 1

            elif instructionCode == '-':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand - rightOperand))
                instructionPointer += 1

            elif instructionCode == '*':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand * rightOperand))
                instructionPointer += 1

            elif instructionCode == '/':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand / rightOperand))
                instructionPointer += 1

            elif instructionCode == '=':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, leftOperand)
                instructionPointer += 1

            elif instructionCode == 'print':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)

                print(leftOperand)
                instructionPointer += 1
            elif instructionCode == '<':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand < rightOperand))
                instructionPointer += 1
            elif instructionCode == '>':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand > rightOperand))
                instructionPointer += 1
            elif instructionCode == '==':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand == rightOperand))
                instructionPointer += 1
            elif instructionCode == '<>':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand != rightOperand))
                instructionPointer += 1
            elif instructionCode == '<=':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand <= rightOperand))
                instructionPointer += 1
            elif instructionCode == '>=':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand >= rightOperand))
                instructionPointer += 1
            elif instructionCode == '&&':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand and rightOperand))
                instructionPointer += 1
            elif instructionCode == '||':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                rightOperand = self.memory.getValueFromVirtualAddress(rightOperandVirtualAddress)

                self.memory.editValueFromVirtualAddress(resultVirtualAddress, (leftOperand or rightOperand))
                instructionPointer += 1
            elif instructionCode == 'GoToF':
                leftOperand = self.memory.getValueFromVirtualAddress(leftOperandVirtualAddress)
                jumpPointer = resultVirtualAddress

                if leftOperand:
                    instructionPointer += 1
                else:
                    instructionPointer = jumpPointer - 1

            elif instructionCode == 'GoTo':
                jumpPointer = resultVirtualAddress
                instructionPointer = jumpPointer - 1
