from generated.MyParser import MyParser
from generated.MyParserVisitor import MyParserVisitor
from utils.values import Int, Float, String


class Interpreter(MyParserVisitor):
    def visitProgram(self, ctx: MyParser.ProgramContext):
        return self.visitChildren(ctx)  # todo

    def visitScopeStatement(self, ctx: MyParser.ScopeStatementContext):
        return self.visitChildren(ctx)  # todo

    def visitSimpleStatement(self, ctx: MyParser.SimpleStatementContext):
        return self.visitChildren(ctx)  # todo

    def visitIfThenElse(self, ctx: MyParser.IfThenElseContext):
        return self.visitChildren(ctx)  # todo

    def visitIf(self, ctx: MyParser.IfContext):
        return self.visitChildren(ctx)  # todo

    def visitThen(self, ctx: MyParser.ThenContext):
        return self.visitChildren(ctx)  # todo

    def visitElse(self, ctx: MyParser.ElseContext):
        return self.visitChildren(ctx)  # todo

    def visitForLoop(self, ctx: MyParser.ForLoopContext):
        return self.visitChildren(ctx)  # todo

    def visitRange(self, ctx: MyParser.RangeContext):
        return self.visitChildren(ctx)  # todo

    def visitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        return self.visitChildren(ctx)  # todo

    def visitComparison(self, ctx: MyParser.ComparisonContext):
        return self.visitChildren(ctx)  # todo

    def visitSimpleAssignment(self, ctx: MyParser.SimpleAssignmentContext):
        return self.visitChildren(ctx)  # todo

    def visitCompoundAssignment(self, ctx: MyParser.CompoundAssignmentContext):
        return self.visitChildren(ctx)  # todo

    def visitPrint(self, ctx: MyParser.PrintContext):
        for i in range(1, len(ctx.children) - 1, 2):
            print(self.visit(ctx.children[i]).value)

    def visitReturn(self, ctx: MyParser.ReturnContext):
        return self.visitChildren(ctx)  # todo

    def visitBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        a = self.visit(ctx.getChild(0))
        b = self.visit(ctx.getChild(2))
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
        return self.visit(ctx.getChild(1))

    def visitTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        return self.visitChildren(ctx)  # todo

    def visitMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        return self.visitChildren(ctx)  # todo

    def visitSingleExpression(self, ctx: MyParser.SingleExpressionContext):
        return self.visit(ctx.getChild(0))

    def visitSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        return self.visitChildren(ctx)  # todo

    def visitBreak(self, ctx: MyParser.BreakContext):
        return self.visitChildren(ctx)  # todo

    def visitContinue(self, ctx: MyParser.ContinueContext):
        return self.visitChildren(ctx)  # todo

    def visitVector(self, ctx: MyParser.VectorContext):
        return self.visitChildren(ctx)  # todo

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
