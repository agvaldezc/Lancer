from VarTable import VarTable

class FunctionDirectory:
	def __init__(self):
		self.functions = {}

	def addFunction(self, functionName):
		self.functions[functionName] = {'parameters': [], 'variables': VarTable() }

	def addParameterTypes(self, functionName, parameterTypeList):
		if self.functionExists(functionName):
			function = self.functions[functionName]
			function['parameters'] += parameterTypeList


	def validateParameters(self, functionName, parameterTypeList):
	    function = self.functions[functionName]
	    
	    if self.functionExists(functionName):
	    	if function['parameters'] == parameterTypeList:
	    		return True
	    	else:
	    		print('Error: Parameter type mismatch.')

	def functionExists(self, functionName):
		if self.functions.has_key(functionName):
			return True
		else:
			print('Error: Function not declared.')
			return False

	def addFunctionVariable(self, functionName, variableName, variableType):
		function = self.functions[functionName]

		if function['variables'].variableExists(variableName):
			print('Error: Variable already declared.')
		else:
			function['variables'].addVariable(variableName,variableType)