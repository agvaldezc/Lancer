# Lancer: Created by Alan Valdez & Rafael Manriquez

# Alan Gustavo Valdez Cascajares A01336955

import ply.lex as lex

# Diccionario de palabras reservadas {palabra : TOKEN}
reserved = {
    'program': 'PROGRAMA',
    'if': 'IF',
    'var': 'VAR',
    'else': 'ELSE',
    'int': 'INT_TYPE',
    'float': 'FLOAT_TYPE',
    'print': 'PRINT',
    'bool': 'BOOL_TYPE',
    'true': 'TRUE',
    'false': 'FALSE',
    'string': 'STRING_TYPE',
    'func': 'FUNC',
    'while': 'WHILE',
    'let': 'CONST',
    'main': 'MAIN',
    'return': 'RETURN',
    'void': 'VOID',
    'drawSquare': 'DRAWSQUARE',
    'drawCircle': 'DRAWCIRCLE',
    'drawLine': 'DRAWLINE',
    'drawPolygon': 'DRAWPOLYGON',
    'drawCurve': 'DRAWCURVE',
    'input': 'INPUT',
    'drawTriangle': 'DRAWTRIANGLE',
    'red': 'RED',
    'green': 'GREEN',
    'blue': 'BLUE',
    'yellow': 'YELLOW',
    'brown': 'BROWN',
    'black': 'BLACK',
    'elseIf': 'ELSEIF'
}

# Lista de tokens
tokens = [
             #	'INTEGER',
             #	'FLOAT',
             #	'BINARY',
             #	'HEX',
             'ID',
             'PLUS',
             'MINUS',
             'TIMES',
             'DIVISION',
             'LPAREN',
             'RPAREN',
             'LBRACKET',
             'RBRACKET',
             'LARRAY',
             'RARRAY',
             'COLON',
             'SEMICOLON',
             'GT',
             'LT',
             'GE',
             'LE',
             'EQUAL',
             'NOT',
             'COMA',
             'AND',
             'OR',
             'DIFFERENT',
             'DOT',
             'ASSIGN',
             'CTEI',
             'CTEF',
             'CTES',
             'CTEB'
         ] + list(reserved.values())

# Expresiones regulares para la definicion de cada token
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVISION = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_LARRAY = r'\['
t_RARRAY = r'\]'
t_GT = r'\>'
t_LT = r'\<'
t_GE = r'\>='
t_LE = r'\<='
t_NOT = r'\!!'
t_EQUAL = r'\=='
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_COMA = r'\,'
t_AND = r'\&&'
t_OR = r'\|\|'
t_DIFFERENT = r'\<>'
t_DOT = r'\.'
t_ASSIGN = r'\='
t_CTES = r'\".*\" | \'.*\''

# t_BINARY = r'[01]+[bB]'
# t_INTEGER = r'[0-9]+'
# t_HEX = '((0[A-Fa-f])|([0-9]))[0-9A-Fa-f]*[Hh]'

# Caracteres a ignorar
t_ignore = ' \t'


# Definicion de token ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'

    # Verificar si el ID es una palabra reservada, si es reservada, cambia el tipo de token al correspondiente
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_CTEF(t):
    r'[0-9]+\.[0-9][0-9]*'
    return t


def t_CTEI(t):
    r'[0-9]+'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Error lexico
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Inicializar lex
lexer = lex.lex()

# # Datos para probar el analizador lexico
# data = 'true'
#
# # Datos como input del analizador lexico
# lexer.input(data)
#
# # Loop que termina al leer todos los caracteres de los datos usados
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print (tok)
