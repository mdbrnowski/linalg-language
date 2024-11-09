from generated.MyParser import MyParser
from generated.MyParserListener import MyParserListener

IND = "|  "


class ASTListener(MyParserListener):
    level = 0

    def enterIf(self, ctx: MyParser.IfContext):
        print(IND * self.level + "if")
        self.level += 1

    def exitIf(self, ctx: MyParser.IfContext):
        self.level -= 1

    def enterThen(self, ctx: MyParser.ThenContext):
        print(IND * self.level + "then")
        self.level += 1

    def exitThen(self, ctx: MyParser.ThenContext):
        self.level -= 1

    def enterElse(self, ctx: MyParser.ElseContext):
        print(IND * self.level + "else")
        self.level += 1

    def exitElse(self, ctx: MyParser.ElseContext):
        self.level -= 1

    def enterForLoop(self, ctx: MyParser.ForLoopContext):
        print(IND * self.level + "for")
        self.level += 1

    def exitForLoop(self, ctx: MyParser.ForLoopContext):
        self.level -= 1

    def enterRange(self, ctx: MyParser.RangeContext):
        print(IND * self.level + "range")
        self.level += 1

    def exitRange(self, ctx: MyParser.RangeContext):
        self.level -= 1

    def enterWhileLoop(self, ctx: MyParser.WhileLoopContext):
        print(IND * self.level + "while")
        self.level += 1

    def exitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        self.level -= 1

    def enterComparison(self, ctx: MyParser.ComparisonContext):
        operator = ctx.getChild(1)
        print(IND * self.level + operator.getText())
        self.level += 1

    def exitComparison(self, ctx: MyParser.ComparisonContext):
        self.level -= 1

    def enterAssignment(self, ctx: MyParser.AssignmentContext):
        operator = ctx.getChild(1)
        print(IND * self.level + operator.getText())
        self.level += 1

    def exitAssignment(self, ctx: MyParser.AssignmentContext):
        self.level -= 1

    def enterPrint(self, ctx: MyParser.PrintContext):
        print(IND * self.level + "print")
        self.level += 1

    def exitPrint(self, ctx: MyParser.PrintContext):
        self.level -= 1

    def enterReturn(self, ctx: MyParser.ReturnContext):
        print(IND * self.level + "return")
        self.level += 1

    def exitReturn(self, ctx: MyParser.ReturnContext):
        self.level -= 1

    def enterBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        operator = ctx.getChild(1)
        print(IND * self.level + operator.getText())
        self.level += 1

    def exitBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        self.level -= 1

    def enterTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        print(IND * self.level + "transpose")
        self.level += 1

    def exitTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        self.level -= 1

    def enterMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        print(IND * self.level + "-")
        self.level += 1

    def exitMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        self.level -= 1

    def enterSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        function_name = ctx.getChild(0)
        print(IND * self.level + function_name.getText())
        self.level += 1

    def exitSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        self.level -= 1

    def enterBreak(self, ctx: MyParser.BreakContext):
        print(IND * self.level + "break")

    def enterContinue(self, ctx: MyParser.ContinueContext):
        print(IND * self.level + "continue")

    def enterVector(self, ctx: MyParser.VectorContext):
        print(IND * self.level + "vector")
        self.level += 1

    def exitVector(self, ctx: MyParser.VectorContext):
        self.level -= 1

    def enterElementReference(self, ctx: MyParser.ElementReferenceContext):
        print(IND * self.level + "ref")
        self.level += 1

    def exitElementReference(self, ctx: MyParser.ElementReferenceContext):
        self.level -= 1

    def enterId(self, ctx: MyParser.IdContext):
        print(IND * self.level + ctx.getText())

    def enterInt(self, ctx: MyParser.IntContext):
        print(IND * self.level + ctx.getText())

    def enterFloat(self, ctx: MyParser.FloatContext):
        print(IND * self.level + ctx.getText())

    def enterString(self, ctx: MyParser.StringContext):
        print(IND * self.level + ctx.getText())
