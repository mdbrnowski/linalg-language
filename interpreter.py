# from antlr4 import ParserRuleContext
from generated.MyParser import MyParser
from generated.MyParserVisitor import MyParserVisitor


class Interpreter(MyParserVisitor):
    def visitProgram(self, ctx: MyParser.ProgramContext):
        print("Program")
        return self.visitChildren(ctx)

    def visitScopeStatement(self, ctx: MyParser.ScopeStatementContext):
        return self.visitChildren(ctx)

    def visitSimpleStatement(self, ctx: MyParser.SimpleStatementContext):
        return self.visitChildren(ctx)

    def visitIfThenElse(self, ctx: MyParser.IfThenElseContext):
        return self.visitChildren(ctx)

    def visitIf(self, ctx: MyParser.IfContext):
        return self.visitChildren(ctx)

    def visitThen(self, ctx: MyParser.ThenContext):
        return self.visitChildren(ctx)

    def visitElse(self, ctx: MyParser.ElseContext):
        return self.visitChildren(ctx)

    def visitForLoop(self, ctx: MyParser.ForLoopContext):
        return self.visitChildren(ctx)

    def visitRange(self, ctx: MyParser.RangeContext):
        return self.visitChildren(ctx)

    def visitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        return self.visitChildren(ctx)

    def visitComparison(self, ctx: MyParser.ComparisonContext):
        return self.visitChildren(ctx)

    def visitSimpleAssignment(self, ctx: MyParser.SimpleAssignmentContext):
        return self.visitChildren(ctx)

    def visitCompoundAssignment(self, ctx: MyParser.CompoundAssignmentContext):
        return self.visitChildren(ctx)

    def visitPrint(self, ctx: MyParser.PrintContext):
        return self.visitChildren(ctx)

    def visitReturn(self, ctx: MyParser.ReturnContext):
        return self.visitChildren(ctx)

    def visitBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        return self.visitChildren(ctx)

    def visitParenthesesExpression(self, ctx: MyParser.ParenthesesExpressionContext):
        return self.visitChildren(ctx)

    def visitTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        return self.visitChildren(ctx)

    def visitMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        return self.visitChildren(ctx)

    def visitSingleExpression(self, ctx: MyParser.SingleExpressionContext):
        return self.visitChildren(ctx)

    def visitSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        return self.visitChildren(ctx)

    def visitBreak(self, ctx: MyParser.BreakContext):
        return self.visitChildren(ctx)

    def visitContinue(self, ctx: MyParser.ContinueContext):
        return self.visitChildren(ctx)

    def visitVector(self, ctx: MyParser.VectorContext):
        return self.visitChildren(ctx)

    def visitElementReference(self, ctx: MyParser.ElementReferenceContext):
        return self.visitChildren(ctx)

    def visitId(self, ctx: MyParser.IdContext):
        return self.visitChildren(ctx)

    def visitInt(self, ctx: MyParser.IntContext):
        return self.visitChildren(ctx)

    def visitFloat(self, ctx: MyParser.FloatContext):
        return self.visitChildren(ctx)

    def visitString(self, ctx: MyParser.StringContext):
        return self.visitChildren(ctx)
