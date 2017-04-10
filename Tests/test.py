from Directories.FunctionDirectory import FunctionDirectory

x = FunctionDirectory()

x.addFunction('funcion1', 'void')
x.addParameterTypes('funcion1', ['Int', 'Float', 'String'])

x.addFunction('funcion2', 'int')
x.addParameterTypes('funcion2', ['Int', 'Float', 'Float'])

parameters = x.functions['funcion1']
parameters2 = x.functions['funcion2']

x.addFunctionVariable('funcion1', 'y', 'Float')

variable = x.getVariable('funcion1', 'x')

print(variable)


