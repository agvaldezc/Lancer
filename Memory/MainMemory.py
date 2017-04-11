from MemorySegment import MemorySegment

class MainMemory:
	def __init__(self):
		self.global_memory = MemorySegment('Global Memory', 1000, 2000)
		self.temp_memory = MemorySegment('Temp Memory', 3000, 2000)
		self.constant_memory = MemorySegment('Constant Memory', 5000, 2000)

	def printMemory(self):
		self.global_memory.printMemory()
		self.temp_memory.printMemory()
		self.constant_memory.printMemory()

	def addGlobalValue(self, value, valueType):
		return self.global_memory.requestMemoryAllocation(value, valueType)

	def addTempValue(self, value, valueType):
		return self.temp_memory.requestMemoryAllocation(value, valueType)

	def addConstantValue(self, value, valueType):
		return self.constant_memory.requestMemoryAllocation(value, valueType)



		