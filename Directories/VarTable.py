class VarTable:
    def __init__(self):
        self.variables = {'total': {'int': 0, 'float': 0, 'bool': 0, 'string': 0}, 'temp_total': {'int': 0, 'float': 0, 'bool': 0, 'string': 0}}

    def addVariable(self, variableName, variableType, variableVirtualAddress):
        self.variables[variableName] = [variableType, variableVirtualAddress]
        self.addVarTotals(variableType)

    def variableExists(self, variableName):
        return self.variables.has_key(variableName)

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

    def getIdByAddress(self, virtualAddress):
        for variable in self.variables:
            if variable != 'total' and variable != 'temp_total':
                variableInfo = self.variables[variable]

                if virtualAddress in variableInfo:
                    return variable



