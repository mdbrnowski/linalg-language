from copy import deepcopy
import sys

from generated.MyParser import MyParser
from generated.MyParserVisitor import MyParserVisitor
from utils.values import Int, Float, String, Vector


class Interpreter(MyParserVisitor):
    def visitProgram(self, ctx: MyParser.ProgramContext):
        return self.visitChildren(ctx)  # todo

    def visitScopeStatement(self, ctx: MyParser.ScopeStatementContext):
        return self.visitChildren(ctx)  # todo

    def visitSimpleStatement(self, ctx: MyParser.SimpleStatementContext):
        return self.visitChildren(ctx)  # todo

    def visitIfThenElse(self, ctx: MyParser.IfThenElseContext):
        condition = self.visit(ctx.if_())
        if condition:
            return self.visit(ctx.then())
        elif ctx.else_() is not None:
            return self.visit(ctx.else_())

    def visitIf(self, ctx: MyParser.IfContext):
        return self.visit(ctx.comparison())

    def visitElse(self, ctx: MyParser.ElseContext):
        return self.visit(ctx.statement())

    def visitForLoop(self, ctx: MyParser.ForLoopContext):
        return self.visitChildren(ctx)  # todo

    def visitRange(self, ctx: MyParser.RangeContext):
        return self.visitChildren(ctx)  # todo

    def visitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        return self.visitChildren(ctx)  # todo

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
        return self.visitChildren(ctx)  # todo

    def visitCompoundAssignment(self, ctx: MyParser.CompoundAssignmentContext):
        return self.visitChildren(ctx)  # todo

    def visitPrint(self, ctx: MyParser.PrintContext):
        for i in range(ctx.getChildCount() // 2):
            print(str(self.visit(ctx.expression(i))))

    def visitReturn(self, ctx: MyParser.ReturnContext):
        if ctx.expression() is not None:
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
        return self.visitChildren(ctx)  # todo

    def visitInt(self, ctx: MyParser.IntContext):
        return Int(ctx.getText())

    def visitFloat(self, ctx: MyParser.FloatContext):
        return Float(ctx.getText())

    def visitString(self, ctx: MyParser.StringContext):
        return String(ctx.getText())
