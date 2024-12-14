import sys
from copy import deepcopy

from generated.MyParser import MyParser
from generated.MyParserVisitor import MyParserVisitor
from utils.memory import MemoryStack
from utils.values import Int, Float, String, Vector


class Interpreter(MyParserVisitor):
    def __init__(self):
        self.memory_stack = MemoryStack()
        self.memory_stack.push_memory()

    def visitScopeStatement(self, ctx: MyParser.ScopeStatementContext):
        self.memory_stack.push_memory()
        self.visitChildren(ctx)
        self.memory_stack.pop_memory()

    def visitIfThenElse(self, ctx: MyParser.IfThenElseContext):
        condition = self.visit(ctx.if_())
        if condition:
            return self.visit(ctx.then())
        elif ctx.else_():
            return self.visit(ctx.else_())

    def visitIf(self, ctx: MyParser.IfContext):
        return self.visit(ctx.comparison())

    def visitElse(self, ctx: MyParser.ElseContext):
        return self.visit(ctx.statement())

    def visitForLoop(self, ctx: MyParser.ForLoopContext):
        a, b = self.visit(ctx.range_())
        variable = ctx.id_().getText()
        while a <= b:
            self.memory_stack.put(variable, Int(a))
            a = a + 1  # to increment enumerateor and disregard changes inside the loop
            self.visit(ctx.statement())

    def visitRange(self, ctx: MyParser.RangeContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        if {type(a), type(b)} != {Int}:
            raise TypeError
        return (a.value, b.value)

    def visitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        while self.visit(ctx.comparison()):
            self.visit(ctx.statement())

    def visitComparison(self, ctx: MyParser.ComparisonContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        match ctx.getChild(1).symbol.type:
            case MyParser.EQ:
                return a == b
            case MyParser.NEQ:
                return a != b
            case MyParser.LT:
                return a < b
            case MyParser.LEQ:
                return a <= b
            case MyParser.GT:
                return a > b
            case MyParser.GEQ:
                return a >= b

    def visitSimpleAssignment(self, ctx: MyParser.SimpleAssignmentContext):
        if ctx.id_():
            self.visitChildren(ctx)
            self.memory_stack.put(ctx.id_().getText(), self.visit(ctx.expression()))
        else:
            pass  # todo

    def visitCompoundAssignment(self, ctx: MyParser.CompoundAssignmentContext):
        if ctx.id_():
            self.visitChildren(ctx)
            old_value = self.memory_stack.get(ctx.id_().getText())
            new_value = self.visit(ctx.expression())
            match ctx.getChild(1).symbol.type:
                case MyParser.ASSIGN_PLUS:
                    new_value = old_value + new_value
                case MyParser.ASSIGN_MINUS:
                    new_value = old_value - new_value
                case MyParser.ASSIGN_MULTIPLY:
                    new_value = old_value * new_value
                case MyParser.ASSIGN_DIVIDE:
                    new_value = old_value / new_value
            self.memory_stack.put(ctx.id_().getText(), new_value)
        else:
            pass  # todo

    def visitPrint(self, ctx: MyParser.PrintContext):
        for i in range(ctx.getChildCount() // 2):
            print(str(self.visit(ctx.expression(i))))

    def visitReturn(self, ctx: MyParser.ReturnContext):
        if ctx.expression():
            return_value = self.visit(ctx.expression())
            if not isinstance(return_value, Int):
                raise TypeError
            sys.exit(return_value.value)
        sys.exit()

    def visitBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        match ctx.op.type:
            case MyParser.PLUS:
                return a + b
            case MyParser.MINUS:
                return a - b
            case MyParser.MULTIPLY:
                return a * b
            case MyParser.DIVIDE:
                return a / b
            # todo: MAT_* operations

    def visitParenthesesExpression(self, ctx: MyParser.ParenthesesExpressionContext):
        return self.visit(ctx.expression())

    def visitTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        vector = self.visit(ctx.expression())
        if not isinstance(vector, Vector):
            raise TypeError
        return vector.transpose()

    def visitMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        return -self.visit(ctx.expression())

    def visitSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        fname = ctx.getChild(0).symbol.type
        if fname == MyParser.EYE:
            dim = self.visit(ctx.expression(0))
            if not isinstance(dim, Int):
                raise TypeError
            rows = [
                Vector([Int(i == j) for j in range(dim.value)])
                for i in range(dim.value)
            ]
            return Vector(rows)
        else:
            dims = [
                self.visit(ctx.expression(i))
                for i in range(ctx.getChildCount() // 2 - 1)
            ]
            if {type(dim) for dim in dims} != {Int}:
                raise TypeError
            vector = {MyParser.ZEROS: Int(0), MyParser.ONES: Int(1)}[fname]
            for dim in reversed(dims):
                vector = Vector([deepcopy(vector) for _ in range(dim.value)])
            return vector

    def visitBreak(self, ctx: MyParser.BreakContext):
        return self.visitChildren(ctx)  # todo

    def visitContinue(self, ctx: MyParser.ContinueContext):
        return self.visitChildren(ctx)  # todo

    def visitVector(self, ctx: MyParser.VectorContext):
        elements = [
            self.visit(ctx.expression(i)) for i in range(ctx.getChildCount() // 2)
        ]
        return Vector(elements)

    def visitElementReference(self, ctx: MyParser.ElementReferenceContext):
        return self.visitChildren(ctx)  # todo

    def visitId(self, ctx: MyParser.IdContext):
        return self.memory_stack.get(ctx.getText())

    def visitInt(self, ctx: MyParser.IntContext):
        return Int(ctx.getText())

    def visitFloat(self, ctx: MyParser.FloatContext):
        return Float(ctx.getText())

    def visitString(self, ctx: MyParser.StringContext):
        return String(ctx.getText()[1:-1])  # without quotes
