class Quadruple:
    def __init__(self, quad_number, operator, left_operand, right_operand, result):
        self.quad_number = quad_number
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result

    def printQuad(self):
        print('Quad {0} = [{1}, {2}, {3}, {4}]'.format(self.quad_number, self.operator, self.left_operand, self.right_operand, self.result))

    def fillJumpQuad(self, quadCounter):
        self.result = quadCounter