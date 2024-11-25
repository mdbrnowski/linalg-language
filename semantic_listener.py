from enum import Enum, auto
from antlr4 import ParserRuleContext
from generated.MyParser import MyParser
from generated.MyParserListener import MyParserListener


class Type(Enum):
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    TBD = auto()  # to be determined (only during assignment)


class SemanticListener(MyParserListener):
    """Checks break and continue statements, variable declarations,types and assignments."""

    def __init__(self):
        self.nested_loop_counter = 0
        self.variables: dict[str, Type | None] = {}
        self.expr_type: dict[
            ParserRuleContext, Type | tuple
        ] = {}  # values are either Type or (Type, int | None, int | None, ...)

    # LOOP CHECKING

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

    def enterRange(self, ctx: MyParser.RangeContext):
        pass

    def exitRange(self, ctx: MyParser.RangeContext):
        pass

    def enterComparison(self, ctx: MyParser.ComparisonContext):
        pass

    def exitComparison(self, ctx: MyParser.ComparisonContext):
        pass

    def enterAssignment(self, ctx: MyParser.AssignmentContext):
        if (
            ctx.getChild(1).symbol.type == MyParser.ASSIGN
            and isinstance(ctx.getChild(0), MyParser.IdContext)
            and ctx.getChild(0).getText() not in self.variables
        ):
            # type is unknown at this point
            self.variables[ctx.getChild(0).getText()] = Type.TBD

    def exitAssignment(self, ctx: MyParser.AssignmentContext):
        if (
            ctx.getChild(1).symbol.type == MyParser.ASSIGN
            and isinstance(ctx.getChild(0), MyParser.IdContext)
            and self.variables[ctx.getChild(0).getText()] is Type.TBD
        ):
            # we finally know the type
            if self.expr_type[ctx.getChild(2)] is Type.TBD:
                ctx.parser.notifyErrorListeners(
                    "Using a variable while declaring it is not allowed",
                    ctx.getChild(1).getSymbol(),
                )
            self.variables[ctx.getChild(0).getText()] = self.expr_type[ctx.getChild(2)]

    def enterBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        pass

    def exitBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        pass

    def exitParenthesesExpression(self, ctx: MyParser.ParenthesesExpressionContext):
        self.expr_type[ctx] = self.expr_type[ctx.getChild(1)]

    def exitTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        matrix = ctx.getChild(0)
        if (  # is a matrix
            isinstance(self.expr_type[matrix], tuple)
            and len(self.expr_type[matrix]) == 3
        ):
            self.expr_type[ctx] = tuple(self.expr_type[matrix][i] for i in (0, 2, 1))
        else:
            ctx.parser.notifyErrorListeners(
                "Transpose operator can only be applied to matrices",
                ctx.getChild(1).getSymbol(),
            )
            self.expr_type[ctx] = self.expr_type[matrix]

    def exitMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        self.expr_type[ctx] = self.expr_type[ctx.getChild(1)]

    def exitSingleExpression(self, ctx: MyParser.SingleExpressionContext):
        self.expr_type[ctx] = self.expr_type[ctx.getChild(0)]

    def exitSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        dimentions = ctx.children[2::2]
        for dim in dimentions:
            if self.expr_type[dim] != Type.INT:
                ctx.parser.notifyErrorListeners(
                    "Matrix dimentions must be integers", ctx.getChild(0).getSymbol()
                )
                self.expr_type[ctx] = None
                break
        type_dimentions = []
        for dim in dimentions:
            if isinstance(dim, MyParser.SingleExpressionContext) and isinstance(
                dim.getChild(0), MyParser.IntContext
            ):
                type_dimentions.append(int(dim.getText()))
            else:
                type_dimentions.append(None)
        self.expr_type[ctx] = (Type.INT, *type_dimentions)

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
        if ctx.getText() not in self.variables:
            ctx.parser.notifyErrorListeners(
                f"Variable {ctx.getText()} not declared", ctx.ID().getSymbol()
            )
            self.expr_type[ctx] = None
        else:
            self.expr_type[ctx] = self.variables[ctx.getText()]

    def enterInt(self, ctx: MyParser.IntContext):
        self.expr_type[ctx] = Type.INT

    def enterFloat(self, ctx: MyParser.FloatContext):
        self.expr_type[ctx] = Type.FLOAT

    def enterString(self, ctx: MyParser.StringContext):
        self.expr_type[ctx] = Type.STRING
