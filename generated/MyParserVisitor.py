# Generated from MyParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyParser import MyParser
else:
    from MyParser import MyParser

# This class defines a complete generic visitor for a parse tree produced by MyParser.

class MyParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyParser#program.
    def visitProgram(self, ctx:MyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#codeBlock.
    def visitCodeBlock(self, ctx:MyParser.CodeBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#ifThenElse.
    def visitIfThenElse(self, ctx:MyParser.IfThenElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#if.
    def visitIf(self, ctx:MyParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#then.
    def visitThen(self, ctx:MyParser.ThenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#else.
    def visitElse(self, ctx:MyParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#forLoop.
    def visitForLoop(self, ctx:MyParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#range.
    def visitRange(self, ctx:MyParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#whileLoop.
    def visitWhileLoop(self, ctx:MyParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#comparison.
    def visitComparison(self, ctx:MyParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#simpleAssignment.
    def visitSimpleAssignment(self, ctx:MyParser.SimpleAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#compoundAssignment.
    def visitCompoundAssignment(self, ctx:MyParser.CompoundAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#print.
    def visitPrint(self, ctx:MyParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#return.
    def visitReturn(self, ctx:MyParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#binaryExpression.
    def visitBinaryExpression(self, ctx:MyParser.BinaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#parenthesesExpression.
    def visitParenthesesExpression(self, ctx:MyParser.ParenthesesExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#transposeExpression.
    def visitTransposeExpression(self, ctx:MyParser.TransposeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#minusExpression.
    def visitMinusExpression(self, ctx:MyParser.MinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#singleExpression.
    def visitSingleExpression(self, ctx:MyParser.SingleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#specialMatrixFunction.
    def visitSpecialMatrixFunction(self, ctx:MyParser.SpecialMatrixFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#break.
    def visitBreak(self, ctx:MyParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#continue.
    def visitContinue(self, ctx:MyParser.ContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#vector.
    def visitVector(self, ctx:MyParser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#elementReference.
    def visitElementReference(self, ctx:MyParser.ElementReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#id.
    def visitId(self, ctx:MyParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#int.
    def visitInt(self, ctx:MyParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#float.
    def visitFloat(self, ctx:MyParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyParser#string.
    def visitString(self, ctx:MyParser.StringContext):
        return self.visitChildren(ctx)



del MyParser