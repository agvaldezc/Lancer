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
