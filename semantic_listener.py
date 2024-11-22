from enum import Enum, auto
from generated.MyParser import MyParser
from generated.MyParserListener import MyParserListener
from antlr4 import ParserRuleContext


class Type(Enum):
    INT = auto()
    FLOAT = auto()
    STRING = auto()


class SemanticListener(MyParserListener):
    """Checks break and continue statements, variable declarations,types and assignments."""

    # LOOP CHECKING

    nested_loop_counter = 0

    def enterForLoop(self, ctx: MyParser.ForLoopContext):
        self.nested_loop_counter += 1

    def exitForLoop(self, ctx: MyParser.ForLoopContext):
        self.nested_loop_counter -= 1

    def enterWhileLoop(self, ctx: MyParser.WhileLoopContext):
        self.nested_loop_counter += 1

    def exitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        self.nested_loop_counter -= 1

    def enterBreak(self, ctx: MyParser.BreakContext):
        if self.nested_loop_counter == 0:
            ctx.parser.notifyErrorListeners(
                "Break statement outside of loop", ctx.BREAK().getSymbol()
            )

    def enterContinue(self, ctx: MyParser.ContinueContext):
        if self.nested_loop_counter == 0:
            ctx.parser.notifyErrorListeners(
                "Continue statement outside of loop", ctx.CONTINUE().getSymbol()
            )

    # VARIABLES & TYPES CHECKING

    variables: dict[str, Type] = {}
    expr_type: dict[
        ParserRuleContext, Type | tuple
    ] = {}  # values are either Type or (Type, int, int, ...)

    def enterRange(self, ctx: MyParser.RangeContext):
        pass

    def exitRange(self, ctx: MyParser.RangeContext):
        pass

    def enterComparison(self, ctx: MyParser.ComparisonContext):
        pass

    def exitComparison(self, ctx: MyParser.ComparisonContext):
        pass

    def enterAssignment(self, ctx: MyParser.AssignmentContext):
        pass

    def exitAssignment(self, ctx: MyParser.AssignmentContext):
        pass

    def enterBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        pass

    def exitBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        pass

    def exitParenthesesExpression(self, ctx: MyParser.ParenthesesExpressionContext):
        self.expr_type[ctx] = self.expr_type[ctx.getChild(1)]

    def enterTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        pass

    def exitTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        pass

    def exitMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        self.expr_type[ctx] = self.expr_type[ctx.getChild(1)]

    def exitSingleExpression(self, ctx: MyParser.SingleExpressionContext):
        self.expr_type[ctx] = self.expr_type[ctx.getChild(0)]

    def enterSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        pass

    def exitSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        pass

    def exitVector(self, ctx: MyParser.VectorContext):
        elements = ctx.children[1::2]
        for i in range(1, len(elements)):
            if self.expr_type[elements[i]] != self.expr_type[elements[i - 1]]:
                wrong_token = ctx.COMMA(i) or ctx.CLOSE_BRACKET_SQUARE()
                ctx.parser.notifyErrorListeners(
                    "Inconsistent types in a vector", wrong_token.getSymbol()
                )
                break
        elem_type = self.expr_type[elements[1]]
        if isinstance(elem_type, Type):
            self.expr_type[ctx] = (elem_type, len(elements))
        else:
            self.expr_type[ctx] = (
                elem_type[0],
                len(elements),
                *elem_type[1:],
            )

    def enterElementReference(self, ctx: MyParser.ElementReferenceContext):
        pass

    def exitElementReference(self, ctx: MyParser.ElementReferenceContext):
        pass

    def enterId(self, ctx: MyParser.IdContext):
        pass

    def enterInt(self, ctx: MyParser.IntContext):
        self.expr_type[ctx] = Type.INT

    def enterFloat(self, ctx: MyParser.FloatContext):
        self.expr_type[ctx] = Type.FLOAT

    def enterString(self, ctx: MyParser.StringContext):
        self.expr_type[ctx] = Type.STRING
