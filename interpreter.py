import sys
from copy import deepcopy

from generated.MyParser import MyParser
from generated.MyParserVisitor import MyParserVisitor
from utils.memory import MemoryStack
from utils.values import Int, Float, String, Vector


class Break(Exception):
    pass


class Continue(Exception):
    pass


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
        for i in range(a, b + 1):
            self.memory_stack.put(variable, Int(i))
            try:
                self.visit(ctx.statement())
            except Continue:
                continue
            except Break:
                break

    def visitRange(self, ctx: MyParser.RangeContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        return (a.value, b.value)

    def visitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        while self.visit(ctx.comparison()):
            try:
                self.visit(ctx.statement())
            except Continue:
                continue
            except Break:
                break

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
        if ctx.id_():  # a = 1
            self.memory_stack.put(ctx.id_().getText(), self.visit(ctx.expression()))
        else:  # a[0] = 1
            ref_value = self.visit(ctx.elementReference())
            new_value = self.visit(ctx.expression())
            ref_value.value = new_value.value

    def visitCompoundAssignment(self, ctx: MyParser.CompoundAssignmentContext):
        if ctx.id_():  # a += 1
            value = self.memory_stack.get(ctx.id_().getText())
            new_value = self.visit(ctx.expression())
            match ctx.getChild(1).symbol.type:
                case MyParser.ASSIGN_PLUS:
                    new_value = value + new_value
                case MyParser.ASSIGN_MINUS:
                    new_value = value - new_value
                case MyParser.ASSIGN_MULTIPLY:
                    new_value = value * new_value
                case MyParser.ASSIGN_DIVIDE:
                    new_value = value / new_value
            self.memory_stack.put(ctx.id_().getText(), new_value)
        else:  # a[0] += 1
            ref_value = self.visit(ctx.elementReference())
            new_value = self.visit(ctx.expression())
            match ctx.getChild(1).symbol.type:
                case MyParser.ASSIGN_PLUS:
                    new_value = ref_value + new_value
                case MyParser.ASSIGN_MINUS:
                    new_value = ref_value - new_value
                case MyParser.ASSIGN_MULTIPLY:
                    new_value = ref_value * new_value
                case MyParser.ASSIGN_DIVIDE:
                    new_value = ref_value / new_value
            ref_value.value = new_value.value

    def visitPrint(self, ctx: MyParser.PrintContext):
        for i in range(ctx.getChildCount() // 2):
            print(str(self.visit(ctx.expression(i))))

    def visitReturn(self, ctx: MyParser.ReturnContext):
        if ctx.expression():
            return_value = self.visit(ctx.expression())
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
            case MyParser.MAT_PLUS:
                return a.mat_add(b)
            case MyParser.MAT_MINUS:
                return a.mat_sub(b)
            case MyParser.MAT_MULTIPLY:
                return a.mat_mul(b)
            case MyParser.MAT_DIVIDE:
                return a.mat_truediv(b)

    def visitParenthesesExpression(self, ctx: MyParser.ParenthesesExpressionContext):
        return self.visit(ctx.expression())

    def visitTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        return self.visit(ctx.expression()).transpose()

    def visitMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        return -self.visit(ctx.expression())

    def visitSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        fname = ctx.getChild(0).symbol.type
        if fname == MyParser.EYE:
            dim = self.visit(ctx.expression(0))
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
            vector = {MyParser.ZEROS: Int(0), MyParser.ONES: Int(1)}[fname]
            for dim in reversed(dims):
                vector = Vector([deepcopy(vector) for _ in range(dim.value)])
            return vector

    def visitBreak(self, ctx: MyParser.BreakContext):
        raise Break()

    def visitContinue(self, ctx: MyParser.ContinueContext):
        raise Continue()

    def visitVector(self, ctx: MyParser.VectorContext):
        elements = [
            self.visit(ctx.expression(i)) for i in range(ctx.getChildCount() // 2)
        ]
        return Vector(elements)

    def visitElementReference(self, ctx: MyParser.ElementReferenceContext):
        indices = [
            self.visit(ctx.expression(i)) for i in range(ctx.getChildCount() // 2 - 1)
        ]
        result = self.visit(ctx.id_())
        for idx in indices:
            result = result.value[idx.value]
        return result

    def visitId(self, ctx: MyParser.IdContext):
        return self.memory_stack.get(ctx.getText())

    def visitInt(self, ctx: MyParser.IntContext):
        return Int(ctx.getText())

    def visitFloat(self, ctx: MyParser.FloatContext):
        return Float(ctx.getText())

    def visitString(self, ctx: MyParser.StringContext):
        return String(ctx.getText()[1:-1])  # without quotes
