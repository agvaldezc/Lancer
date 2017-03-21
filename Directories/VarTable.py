class VarTable:
    def __init__(self):
        self.variables = {}

    def addVariable(self, variableName, variableType):
        self.variables[variableName] = variableType

    def variableExists(self, variableName):
        if self.variables.has_key(variableName):
            return True
        else:
            return False

    def getVariable(self, variableName):
        if self.variables.has_key(variableName):
            return (variableName, self.variables[variableName])
        else:
            return None



