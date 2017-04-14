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
                    "&&" : "error",
                    "||" : "error"
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
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "<>" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },
                "string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "<>": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "&&": "error",
                    "||": "error"
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
                    "&&" : "error",
                    "||" : "error"
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
                    "&&" : "error",
                    "||" : "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "<>" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },
                "string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "<>": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "&&": "error",
                    "||": "error"
                }
            },
            "bool" : {
                "int" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "<>" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },
                "float" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "error",
                    "==" : "error",
                    "<>" : "error",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "&&" : "error",
                    "||" : "error"
                },
                "bool" : {
                    "+" : "error",
                    "-" : "error",
                    "*" : "error",
                    "/" : "error",
                    "=" : "bool",
                    "==" : "bool",
                    "<>" : "bool",
                    ">" : "error",
                    "<" : "error",
                    ">=" : "error",
                    "<=" : "error",
                    "&&" : "bool",
                    "||" : "bool"
                },
                "string": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "<>": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "&&": "error",
                    "||": "error"
                }
            },
            "string": {
                "int": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "<>": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "&&": "error",
                    "||": "error"
                },
                "float": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "<>": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "&&": "error",
                    "||": "error"
                },
                "bool": {
                    "+": "error",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "error",
                    "<>": "error",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "&&": "error",
                    "||": "error"
                },
                "string": {
                    "+": "string",
                    "-": "error",
                    "*": "error",
                    "/": "error",
                    "=": "error",
                    "==": "string",
                    "<>": "string",
                    ">": "error",
                    "<": "error",
                    ">=": "error",
                    "<=": "error",
                    "&&": "error",
                    "||": "error"
                }
            }
        }

    def getSemanticType(self, type1, type2, operator):
        return self.cube[type1][type2][operator]
