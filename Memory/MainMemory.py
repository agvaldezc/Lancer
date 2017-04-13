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

    def getValueFromVirtualAddress(self, virtualAddress):
        if virtualAddress >= self.global_memory.initial_address and virtualAddress <= self.global_memory.final_address:
            return self.global_memory.getValueFromVirtualAddress(virtualAddress)

        if virtualAddress >= self.temp_memory.initial_address and virtualAddress <= self.temp_memory.final_address:
            return self.temp_memory.getValueFromVirtualAddress(virtualAddress)

        if virtualAddress >= self.constant_memory.initial_address and virtualAddress <= self.constant_memory.final_address:
            return self.constant_memory.getValueFromVirtualAddress(virtualAddress)

    def editValueFromVirtualAddress(self, virtualAddress, value):
        if virtualAddress >= self.global_memory.initial_address and virtualAddress <= self.global_memory.final_address:
            self.global_memory.editValue(virtualAddress, value)
        elif virtualAddress >= self.temp_memory.initial_address and virtualAddress <= self.temp_memory.final_address:
            self.temp_memory.editValue(virtualAddress, value)
        else:
            self.constant_memory.editValue(virtualAddress, value)