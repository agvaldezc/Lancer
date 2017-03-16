class SemanticCubeDict:
    def __init__(self):
        self.cube = {
            "int" : {
                "int" : {
                    "+" : "int",
                    "-" : "int",
                    "*" : "int",
                    "/" : "int",
                    "=" : "int",
                    "==" : "bool",
                    "<>" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    "&&" : "ERROR",
                    "||" : "ERROR"
                },
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "=" : "float",
                    "==" : "bool",
                    "<>" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    "&&" : "",
                    "||" : ""
                },
                "bool" : {
                    "+" : "ERROR",
                    "-" : "ERROR",
                    "*" : "ERROR",
                    "/" : "ERROR",
                    "=" : "ERROR",
                    "==" : "ERROR",
                    "<>" : "ERROR",
                    ">" : "ERROR",
                    "<" : "ERROR",
                    ">=" : "ERROR",
                    "<=" : "ERROR",
                    "&&" : "ERROR",
                    "||" : "ERROR"
                },
                "string": {
                    "+": "ERROR",
                    "-": "ERROR",
                    "*": "ERROR",
                    "/": "ERROR",
                    "=": "ERROR",
                    "==": "ERROR",
                    "<>": "ERROR",
                    ">": "ERROR",
                    "<": "ERROR",
                    ">=": "ERROR",
                    "<=": "ERROR",
                    "&&": "ERROR",
                    "||": "ERROR"
                }
            },
            "float" : {
                "int" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "=" : "float",
                    "==" : "bool",
                    "<>" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    "&&" : "ERROR",
                    "||" : "ERROR"
                },
                "float" : {
                    "+" : "float",
                    "-" : "float",
                    "*" : "float",
                    "/" : "float",
                    "=" : "float",
                    "==" : "bool",
                    "<>" : "bool",
                    ">" : "bool",
                    "<" : "bool",
                    ">=" : "bool",
                    "<=" : "bool",
                    "&&" : "ERROR",
                    "||" : "ERROR"
                },
                "bool" : {
                    "+" : "ERROR",
                    "-" : "ERROR",
                    "*" : "ERROR",
                    "/" : "ERROR",
                    "=" : "ERROR",
                    "==" : "ERROR",
                    "<>" : "ERROR",
                    ">" : "ERROR",
                    "<" : "ERROR",
                    ">=" : "ERROR",
                    "<=" : "ERROR",
                    "&&" : "ERROR",
                    "||" : "ERROR"
                },
                "string": {
                    "+": "ERROR",
                    "-": "ERROR",
                    "*": "ERROR",
                    "/": "ERROR",
                    "=": "ERROR",
                    "==": "ERROR",
                    "<>": "ERROR",
                    ">": "ERROR",
                    "<": "ERROR",
                    ">=": "ERROR",
                    "<=": "ERROR",
                    "&&": "ERROR",
                    "||": "ERROR"
                }
            },
            "bool" : {
                "int" : {
                    "+" : "ERROR",
                    "-" : "ERROR",
                    "*" : "ERROR",
                    "/" : "ERROR",
                    "=" : "ERROR",
                    "==" : "ERROR",
                    "<>" : "ERROR",
                    ">" : "ERROR",
                    "<" : "ERROR",
                    ">=" : "ERROR",
                    "<=" : "ERROR",
                    "&&" : "ERROR",
                    "||" : "ERROR"
                },
                "float" : {
                    "+" : "ERROR",
                    "-" : "ERROR",
                    "*" : "ERROR",
                    "/" : "ERROR",
                    "=" : "ERROR",
                    "==" : "ERROR",
                    "<>" : "ERROR",
                    ">" : "ERROR",
                    "<" : "ERROR",
                    ">=" : "ERROR",
                    "<=" : "ERROR",
                    "&&" : "ERROR",
                    "||" : "ERROR"
                },
                "bool" : {
                    "+" : "ERROR",
                    "-" : "ERROR",
                    "*" : "ERROR",
                    "/" : "ERROR",
                    "=" : "ERROR",
                    "==" : "bool",
                    "<>" : "bool",
                    ">" : "ERROR",
                    "<" : "ERROR",
                    ">=" : "ERROR",
                    "<=" : "ERROR",
                    "&&" : "bool",
                    "||" : "bool"
                },
                "string": {
                    "+": "ERROR",
                    "-": "ERROR",
                    "*": "ERROR",
                    "/": "ERROR",
                    "=": "ERROR",
                    "==": "ERROR",
                    "<>": "ERROR",
                    ">": "ERROR",
                    "<": "ERROR",
                    ">=": "ERROR",
                    "<=": "ERROR",
                    "&&": "ERROR",
                    "||": "ERROR"
                }
            },
            "string": {
                "int": {
                    "+": "ERROR",
                    "-": "ERROR",
                    "*": "ERROR",
                    "/": "ERROR",
                    "=": "ERROR",
                    "==": "ERROR",
                    "<>": "ERROR",
                    ">": "ERROR",
                    "<": "ERROR",
                    ">=": "ERROR",
                    "<=": "ERROR",
                    "&&": "ERROR",
                    "||": "ERROR"
                },
                "float": {
                    "+": "ERROR",
                    "-": "ERROR",
                    "*": "ERROR",
                    "/": "ERROR",
                    "=": "ERROR",
                    "==": "ERROR",
                    "<>": "ERROR",
                    ">": "ERROR",
                    "<": "ERROR",
                    ">=": "ERROR",
                    "<=": "ERROR",
                    "&&": "ERROR",
                    "||": "ERROR"
                },
                "bool": {
                    "+": "ERROR",
                    "-": "ERROR",
                    "*": "ERROR",
                    "/": "ERROR",
                    "=": "ERROR",
                    "==": "ERROR",
                    "<>": "ERROR",
                    ">": "ERROR",
                    "<": "ERROR",
                    ">=": "ERROR",
                    "<=": "ERROR",
                    "&&": "ERROR",
                    "||": "ERROR"
                },
                "string": {
                    "+": "string",
                    "-": "ERROR",
                    "*": "ERROR",
                    "/": "ERROR",
                    "=": "ERROR",
                    "==": "string",
                    "<>": "string",
                    ">": "ERROR",
                    "<": "ERROR",
                    ">=": "ERROR",
                    "<=": "ERROR",
                    "&&": "ERROR",
                    "||": "ERROR"
                }
            }
        }

    def getSemanticType(self, type1, type2, operator):
        return self.cube[type1][type2][operator]

cube = SemanticCubeDict()

print(cube.getSemanticType('float', 'string', '*'))
