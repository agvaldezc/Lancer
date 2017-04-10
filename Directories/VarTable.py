class VarTable:
    def __init__(self):
        self.variables = {'total': {'int': 0, 'float': 0, 'bool': 0, 'string': 0}, 'temp_total': {'int': 0, 'float': 0, 'bool': 0, 'string': 0}}

    def addVariable(self, variableName, variableType):
        self.variables[variableName] = variableType
        self.addVarTotals(variableType)

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

    def getVarTotals(self):
        return self.variables['total']

    def addVarTotals(self, variableType):
        totals = self.variables['total']
        totals[variableType] += 1

    def addTempType(self, variableType):
        temp_totals = self.variables['temp_total']
        temp_totals[variableType] += 1



