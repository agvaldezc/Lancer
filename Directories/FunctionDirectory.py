from VarTable import VarTable

class FunctionDirectory:
    def __init__(self):
        self.functions = {}

    def addFunction(self, functionName, functionType):
        self.functions[functionName] = {'parameters': [], 'variables': VarTable(), 'type' : functionType }

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
                sys.exit(ERROR_CODES['type_mismatch'])

    def functionExists(self, functionName):
        return self.functions.has_key(functionName)

    def addFunctionVariable(self, functionName, variableName, variableType):
        function = self.functions[functionName]

        if function['variables'].variableExists(variableName):
            print('Error: Variable already declared.')
            sys.exit(ERROR_CODES['variable_already_declared'])
            return False
        else:
            function['variables'].addVariable(variableName,variableType)
            return True

    def getVariable(self, functionName, variableName):
        function = self.functions[functionName]
        variables = function["variables"]

        variable = variables.getVariable(variableName)

        return variable
