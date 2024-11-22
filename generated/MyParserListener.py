# Generated from MyParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyParser import MyParser
else:
    from MyParser import MyParser

# This class defines a complete listener for a parse tree produced by MyParser.
class MyParserListener(ParseTreeListener):

    # Enter a parse tree produced by MyParser#program.
    def enterProgram(self, ctx:MyParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyParser#program.
    def exitProgram(self, ctx:MyParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyParser#codeBlock.
    def enterCodeBlock(self, ctx:MyParser.CodeBlockContext):
        pass

    # Exit a parse tree produced by MyParser#codeBlock.
    def exitCodeBlock(self, ctx:MyParser.CodeBlockContext):
        pass


    # Enter a parse tree produced by MyParser#ifThenElse.
    def enterIfThenElse(self, ctx:MyParser.IfThenElseContext):
        pass

    # Exit a parse tree produced by MyParser#ifThenElse.
    def exitIfThenElse(self, ctx:MyParser.IfThenElseContext):
        pass


    # Enter a parse tree produced by MyParser#if.
    def enterIf(self, ctx:MyParser.IfContext):
        pass

    # Exit a parse tree produced by MyParser#if.
    def exitIf(self, ctx:MyParser.IfContext):
        pass


    # Enter a parse tree produced by MyParser#then.
    def enterThen(self, ctx:MyParser.ThenContext):
        pass

    # Exit a parse tree produced by MyParser#then.
    def exitThen(self, ctx:MyParser.ThenContext):
        pass


    # Enter a parse tree produced by MyParser#else.
    def enterElse(self, ctx:MyParser.ElseContext):
        pass

    # Exit a parse tree produced by MyParser#else.
    def exitElse(self, ctx:MyParser.ElseContext):
        pass


    # Enter a parse tree produced by MyParser#forLoop.
    def enterForLoop(self, ctx:MyParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MyParser#forLoop.
    def exitForLoop(self, ctx:MyParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MyParser#range.
    def enterRange(self, ctx:MyParser.RangeContext):
        pass

    # Exit a parse tree produced by MyParser#range.
    def exitRange(self, ctx:MyParser.RangeContext):
        pass


    # Enter a parse tree produced by MyParser#whileLoop.
    def enterWhileLoop(self, ctx:MyParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by MyParser#whileLoop.
    def exitWhileLoop(self, ctx:MyParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by MyParser#comparison.
    def enterComparison(self, ctx:MyParser.ComparisonContext):
        pass

    # Exit a parse tree produced by MyParser#comparison.
    def exitComparison(self, ctx:MyParser.ComparisonContext):
        pass


    # Enter a parse tree produced by MyParser#assignment.
    def enterAssignment(self, ctx:MyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MyParser#assignment.
    def exitAssignment(self, ctx:MyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MyParser#print.
    def enterPrint(self, ctx:MyParser.PrintContext):
        pass

    # Exit a parse tree produced by MyParser#print.
    def exitPrint(self, ctx:MyParser.PrintContext):
        pass


    # Enter a parse tree produced by MyParser#return.
    def enterReturn(self, ctx:MyParser.ReturnContext):
        pass

    # Exit a parse tree produced by MyParser#return.
    def exitReturn(self, ctx:MyParser.ReturnContext):
        pass


    # Enter a parse tree produced by MyParser#binaryExpression.
    def enterBinaryExpression(self, ctx:MyParser.BinaryExpressionContext):
        pass

    # Exit a parse tree produced by MyParser#binaryExpression.
    def exitBinaryExpression(self, ctx:MyParser.BinaryExpressionContext):
        pass


    # Enter a parse tree produced by MyParser#parenthesesExpression.
    def enterParenthesesExpression(self, ctx:MyParser.ParenthesesExpressionContext):
        pass

    # Exit a parse tree produced by MyParser#parenthesesExpression.
    def exitParenthesesExpression(self, ctx:MyParser.ParenthesesExpressionContext):
        pass


    # Enter a parse tree produced by MyParser#transposeExpression.
    def enterTransposeExpression(self, ctx:MyParser.TransposeExpressionContext):
        pass

    # Exit a parse tree produced by MyParser#transposeExpression.
    def exitTransposeExpression(self, ctx:MyParser.TransposeExpressionContext):
        pass


    # Enter a parse tree produced by MyParser#minusExpression.
    def enterMinusExpression(self, ctx:MyParser.MinusExpressionContext):
        pass

    # Exit a parse tree produced by MyParser#minusExpression.
    def exitMinusExpression(self, ctx:MyParser.MinusExpressionContext):
        pass


    # Enter a parse tree produced by MyParser#singleExpression.
    def enterSingleExpression(self, ctx:MyParser.SingleExpressionContext):
        pass

    # Exit a parse tree produced by MyParser#singleExpression.
    def exitSingleExpression(self, ctx:MyParser.SingleExpressionContext):
        pass


    # Enter a parse tree produced by MyParser#specialMatrixFunction.
    def enterSpecialMatrixFunction(self, ctx:MyParser.SpecialMatrixFunctionContext):
        pass

    # Exit a parse tree produced by MyParser#specialMatrixFunction.
    def exitSpecialMatrixFunction(self, ctx:MyParser.SpecialMatrixFunctionContext):
        pass


    # Enter a parse tree produced by MyParser#break.
    def enterBreak(self, ctx:MyParser.BreakContext):
        pass

    # Exit a parse tree produced by MyParser#break.
    def exitBreak(self, ctx:MyParser.BreakContext):
        pass


    # Enter a parse tree produced by MyParser#continue.
    def enterContinue(self, ctx:MyParser.ContinueContext):
        pass

    # Exit a parse tree produced by MyParser#continue.
    def exitContinue(self, ctx:MyParser.ContinueContext):
        pass


    # Enter a parse tree produced by MyParser#vector.
    def enterVector(self, ctx:MyParser.VectorContext):
        pass

    # Exit a parse tree produced by MyParser#vector.
    def exitVector(self, ctx:MyParser.VectorContext):
        pass


    # Enter a parse tree produced by MyParser#elementReference.
    def enterElementReference(self, ctx:MyParser.ElementReferenceContext):
        pass

    # Exit a parse tree produced by MyParser#elementReference.
    def exitElementReference(self, ctx:MyParser.ElementReferenceContext):
        pass


    # Enter a parse tree produced by MyParser#id.
    def enterId(self, ctx:MyParser.IdContext):
        pass

    # Exit a parse tree produced by MyParser#id.
    def exitId(self, ctx:MyParser.IdContext):
        pass


    # Enter a parse tree produced by MyParser#int.
    def enterInt(self, ctx:MyParser.IntContext):
        pass

    # Exit a parse tree produced by MyParser#int.
    def exitInt(self, ctx:MyParser.IntContext):
        pass


    # Enter a parse tree produced by MyParser#float.
    def enterFloat(self, ctx:MyParser.FloatContext):
        pass

    # Exit a parse tree produced by MyParser#float.
    def exitFloat(self, ctx:MyParser.FloatContext):
        pass


    # Enter a parse tree produced by MyParser#string.
    def enterString(self, ctx:MyParser.StringContext):
        pass

    # Exit a parse tree produced by MyParser#string.
    def exitString(self, ctx:MyParser.StringContext):
        pass



del MyParser