import sys


class MemorySegment:
    def __init__(self, memory_name, offset, total_records):

        partitionSize = total_records / 4

        self.memory_name = memory_name
        self.offset = offset
        self.initial_address = offset
        self.final_address = (offset + total_records) - 1
        self.int_initial_address = 0
        self.int_final_address = partitionSize - 1
        self.float_initial_address = partitionSize
        self.float_final_address = (partitionSize * 2) - 1
        self.bool_initial_address = (partitionSize * 2)
        self.bool_final_address = (partitionSize * 3) - 1
        self.string_initial_address = (partitionSize * 3)
        self.string_final_address = (partitionSize * 4) - 1
        self.current_int_address = self.int_initial_address
        self.current_float_address = self.float_initial_address
        self.current_bool_address = self.bool_initial_address
        self.current_string_address = self.string_initial_address
        self.int_segment = {}
        self.float_segment = {}
        self.bool_segment = {}
        self.string_segment = {}

    def printMemory(self):
        print("{0}".format(self.memory_name))
        print("Memory offset: {0}".format(self.offset))
        print("Memory initial address: {0}".format(self.initial_address))
        print("Memory final address: {0}".format(self.final_address))
        print("Memory int initial address: {0}".format(self.int_initial_address))
        print("Memory int final address: {0}".format(self.int_final_address))
        print("Memory float initial address: {0}".format(self.float_initial_address))
        print("Memory float final address: {0}".format(self.float_final_address))
        print("Memory bool initial address: {0}".format(self.bool_initial_address))
        print("Memory bool final address: {0}".format(self.bool_final_address))
        print("Memory string initial address: {0}".format(self.string_initial_address))
        print("Memory string final address: {0}".format(self.string_final_address))
        print("Memory int current pointer: {0}".format(self.current_int_address))
        print("Memory float current pointer: {0}".format(self.current_float_address))
        print("Memory bool current pointer: {0}".format(self.current_bool_address))
        print("Memory string current pointer: {0}".format(self.current_string_address))
        print("Memory int segment: {0}".format(self.int_segment))
        print("Memory float segment: {0}".format(self.float_segment))
        print("Memory bool segment: {0}".format(self.bool_segment))
        print("Memory string segment: {0}".format(self.string_segment))

    def requestMemoryAllocation(self, value, valueType):
        if valueType == 'int':
            if self.current_int_address >= self.int_initial_address and self.current_int_address <= self.int_final_address:
                address = self.current_int_address + self.offset
                self.int_segment[self.current_int_address] = value
                self.current_int_address += 1
                return address
            else:
                return None

        if valueType == 'float':
            if self.current_float_address >= self.float_initial_address and self.current_float_address <= self.float_final_address:
                address = self.current_float_address + self.offset
                self.float_segment[self.current_float_address] = value
                self.current_float_address += 1
                return address
            else:
                return None

        if valueType == 'bool':
            if self.current_bool_address >= self.bool_initial_address and self.current_bool_address <= self.bool_final_address:
                address = self.current_bool_address + self.offset
                self.bool_segment[self.current_bool_address] = value
                self.current_bool_address += 1
                return address
            else:
                return None

        if valueType == 'string':
            if self.current_string_address >= self.string_initial_address and self.current_string_address <= self.string_final_address:
                address = self.current_string_address + self.offset
                self.string_segment[self.current_string_address] = value
                self.current_string_address += 1
                return address
            else:
                return None

    def resetMemory(self):
        self.current_int_address = self.int_initial_address
        self.current_float_address = self.float_initial_address
        self.current_bool_address = self.bool_initial_address
        self.current_string_address = self.string_initial_address

    def editValue(self, virtualAddress, value):
        address = virtualAddress - self.offset

        if address >= self.int_initial_address and address <= self.int_final_address:
            self.int_segment[address] = value

        if address >= self.float_initial_address and address <= self.float_final_address:
            self.float_segment[address] = value

        if address >= self.bool_initial_address and address <= self.bool_final_address:
            self.bool_segment[address] = value

        if address >= self.string_initial_address and address <= self.string_final_address:
            self.string_segment[address] = value

    def getValueFromVirtualAddress(self, virtualAddress):
        realAddress = virtualAddress - self.offset

        if realAddress >= self.int_initial_address and realAddress <= self.int_final_address:
            return self.int_segment[realAddress]

        if realAddress >= self.float_initial_address and realAddress <= self.float_final_address:
            return self.float_segment[realAddress]

        if realAddress >= self.bool_initial_address and realAddress <= self.bool_final_address:
            return self.bool_segment[realAddress]

        if realAddress >= self.string_initial_address and realAddress <= self.string_final_address:
            return self.string_segment[realAddress]

    def requestDimensionVariableMemoryAllocation(self, dimensionSize, valueType, value):
        if valueType == 'int':
            addressBlock = self.current_int_address + dimensionSize

            if addressBlock >= self.int_initial_address and addressBlock <= self.int_final_address:
                baseAddress = self.current_int_address + self.offset

                index = 0

                while index <= dimensionSize:
                    self.int_segment[self.current_int_address] = value
                    self.current_int_address += 1
                    index += 1
                return baseAddress
            else:
                return None

        if valueType == 'float':
            addressBlock = self.current_float_address + dimensionSize

            if addressBlock >= self.float_initial_address and addressBlock <= self.float_final_address:
                baseAddress = self.current_float_address + self.offset

                index = 0

                while index <= dimensionSize:
                    self.float_segment[self.current_float_address] = value
                    self.current_float_address += 1
                    index += 1
                return baseAddress
            else:
                return None

        if valueType == 'bool':
            addressBlock = self.current_bool_address + dimensionSize

            if addressBlock >= self.bool_initial_address and addressBlock <= self.bool_final_address:
                baseAddress = self.current_bool_address + self.offset

                index = 0

                while index <= dimensionSize:
                    self.bool_segment[self.current_bool_address] = value
                    self.current_bool_address += 1
                    index += 1
                return baseAddress
            else:
                return None

        if valueType == 'string':
            addressBlock = self.current_string_address + dimensionSize

            if addressBlock >= self.string_initial_address and addressBlock <= self.string_final_address:
                baseAddress = self.current_string_address + self.offset

                index = 0

                while index <= dimensionSize:
                    self.string_segment[self.current_string_address] = value
                    self.current_string_address += 1
                    index += 1
                return baseAddress
            else:
                return None