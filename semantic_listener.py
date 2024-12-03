from enum import Enum, auto
from antlr4 import ParserRuleContext
from generated.MyParser import MyParser
from generated.MyParserListener import MyParserListener


class Type(Enum):
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    TBD = auto()  # to be determined (only during assignment)


def is_plain_integer(ctx: ParserRuleContext) -> bool:
    return isinstance(ctx, MyParser.SingleExpressionContext) and isinstance(
        ctx.getChild(0), MyParser.IntContext
    )


def get_resulting_type(
    type_1: Type | tuple | None, operator: int, type_2: Type | tuple | None
) -> Type | tuple | None:
    if operator in [
        MyParser.PLUS,
        MyParser.MINUS,
        MyParser.MULTIPLY,
        MyParser.DIVIDE,
    ]:
        if {type_1, type_2} == {Type.INT}:
            return Type.INT
        if {type_1, type_2} <= {Type.FLOAT, Type.INT}:
            return Type.FLOAT
    else:
        if type_1 == type_2:
            return type_1
    return None


class SemanticListener(MyParserListener):
    """Checks break and continue statements, variable declarations, types, assignments, etc."""

    def __init__(self):
        self.nested_loop_counter = 0
        self.variables: dict[str, Type | tuple | None] = {}
        self.expr_type: dict[
            ParserRuleContext, Type | tuple | None
        ] = {}  # values should be either Type or (Type, int | None, int | None, ...)

    def enterForLoop(self, ctx: MyParser.ForLoopContext):
        self.nested_loop_counter += 1
        var = ctx.getChild(1).getText()
        if var in self.variables:
            ctx.parser.notifyErrorListeners(
                f"Variable {var} already declared", ctx.getChild(2).getSymbol()
            )
        else:
            self.variables[var] = Type.INT

    def exitForLoop(self, ctx: MyParser.ForLoopContext):
        self.nested_loop_counter -= 1

    def exitRange(self, ctx: MyParser.RangeContext):
        children_types = {self.expr_type[ctx.getChild(i)] for i in [0, 2]}
        if children_types != {Type.INT}:
            ctx.parser.notifyErrorListeners(
                "Range bounds must be integers", ctx.getChild(1).getSymbol()
            )
            self.expr_type[ctx] = None

    def enterWhileLoop(self, ctx: MyParser.WhileLoopContext):
        self.nested_loop_counter += 1

    def exitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        self.nested_loop_counter -= 1

    def exitComparison(self, ctx: MyParser.ComparisonContext):
        children_types = {self.expr_type[ctx.getChild(i)] for i in [0, 2]}
        if not (
            children_types <= {Type.INT, Type.FLOAT}
            or (
                ctx.getChild(1).symbol.type in {MyParser.EQ, MyParser.NE}
                and children_types <= {Type.STRING}
            )
        ):
            ctx.parser.notifyErrorListeners(
                "Incompatible types in a comparison", ctx.getChild(1).getSymbol()
            )
            self.expr_type[ctx] = None

    def enterSimpleAssignment(self, ctx: MyParser.SimpleAssignmentContext):
        if (
            isinstance(ctx.getChild(0), MyParser.IdContext)
            and ctx.getChild(0).getText() not in self.variables
        ):
            self.variables[ctx.getChild(0).getText()] = Type.TBD

    def exitSimpleAssignment(self, ctx: MyParser.SimpleAssignmentContext):
        if (
            isinstance(ctx.getChild(0), MyParser.IdContext)
            and self.variables[(var := ctx.getChild(0).getText())] is Type.TBD
        ):
            if self.expr_type[ctx.getChild(2)] is Type.TBD:
                ctx.parser.notifyErrorListeners(
                    "Using a variable while declaring it is not allowed",
                    ctx.getChild(1).getSymbol(),
                )
                self.variables[var] = None
                self.expr_type[ctx.getChild(0)] = None
            else:
                self.variables[var] = self.expr_type[ctx.getChild(2)]
                self.expr_type[ctx.getChild(0)] = self.expr_type[ctx.getChild(2)]

        elif self.expr_type[ctx.getChild(0)] != self.expr_type[ctx.getChild(2)]:
            ctx.parser.notifyErrorListeners(
                "Incompatible types in an assignment", ctx.getChild(1).getSymbol()
            )

    def exitCompoundAssignment(self, ctx: MyParser.CompoundAssignmentContext):
        type_1 = self.expr_type[ctx.getChild(0)]
        type_2 = self.expr_type[ctx.getChild(2)]
        operator = {
            MyParser.ASSIGN_PLUS: MyParser.PLUS,
            MyParser.ASSIGN_MINUS: MyParser.MINUS,
            MyParser.ASSIGN_MULTIPLY: MyParser.MULTIPLY,
            MyParser.ASSIGN_DIVIDE: MyParser.DIVIDE,
        }[ctx.getChild(1).symbol.type]
        resulting_type = get_resulting_type(type_1, operator, type_2)
        if resulting_type is None:
            ctx.parser.notifyErrorListeners(
                "Incompatible types in a compound assignment",
                ctx.getChild(1).getSymbol(),
            )
        elif resulting_type is not type_1:
            ctx.parser.notifyErrorListeners(
                "Cannot change type in a compound assignment",
                ctx.getChild(1).getSymbol(),
            )

    def exitBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        type_1 = self.expr_type[ctx.getChild(0)]
        type_2 = self.expr_type[ctx.getChild(2)]
        operator = ctx.op.type
        self.expr_type[ctx] = get_resulting_type(type_1, operator, type_2)
        if self.expr_type[ctx] is None:
            ctx.parser.notifyErrorListeners(
                "Incompatible types in a binary operation",
                ctx.getChild(1).getSymbol(),
            )

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
                return
        type_dimentions = []
        for dim in dimentions:
            if is_plain_integer(dim):
                type_dimentions.append(int(dim.getText()))
            else:
                type_dimentions.append(None)
        if ctx.getChild(0).symbol.type == MyParser.EYE:
            assert len(type_dimentions) == 1
            self.expr_type[ctx] = (Type.INT, type_dimentions[0], type_dimentions[0])
        else:
            self.expr_type[ctx] = (Type.INT, *type_dimentions)

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

    def exitVector(self, ctx: MyParser.VectorContext):
        elements = ctx.children[1::2]
        for i in range(1, len(elements)):
            if self.expr_type[elements[i]] != self.expr_type[elements[i - 1]]:
                wrong_token = ctx.COMMA(i) or ctx.CLOSE_BRACKET_SQUARE()
                ctx.parser.notifyErrorListeners(
                    "Inconsistent types in a vector", wrong_token.getSymbol()
                )
                self.expr_type[ctx] = None
                return
        elem_type = self.expr_type[elements[1]]
        if isinstance(elem_type, Type):
            self.expr_type[ctx] = (elem_type, len(elements))
        else:
            self.expr_type[ctx] = (
                elem_type[0],
                len(elements),
                *elem_type[1:],
            )

    def exitElementReference(self, ctx: MyParser.ElementReferenceContext):
        references: list[ParserRuleContext] = ctx.children[2::2]
        for ref in references:
            if self.expr_type[ref] != Type.INT:
                ctx.parser.notifyErrorListeners(
                    "Indices must be integers", ctx.getChild(1).getSymbol()
                )
                self.expr_type[ctx] = None
                return
        id_type = self.expr_type[ctx.getChild(0)]
        if not isinstance(id_type, tuple):
            ctx.parser.notifyErrorListeners(
                "Indexing can only be applied to tensors", ctx.getChild(1).getSymbol()
            )
            self.expr_type[ctx] = None
            return
        elif len(references) > len(id_type) - 1:
            ctx.parser.notifyErrorListeners(
                "Too many indices", ctx.getChild(1).getSymbol()
            )
            self.expr_type[ctx] = None
            return
        elif len(references) < len(id_type) - 1:
            self.expr_type[ctx] = (id_type[0], *id_type[1 + len(references) :])
        else:
            self.expr_type[ctx] = id_type[0]

        for i, ref in enumerate(references):
            if is_plain_integer(ref) and id_type[i + 1] is not None:
                if int(ref.getText()) >= id_type[i + 1]:
                    ctx.parser.notifyErrorListeners(
                        "Index out of bounds", ref.getChild(0).getChild(0).getSymbol()
                    )

    def exitId(self, ctx: MyParser.IdContext):
        if ctx.getText() not in self.variables:
            ctx.parser.notifyErrorListeners(
                f"Variable {ctx.getText()} not declared", ctx.ID().getSymbol()
            )
            self.expr_type[ctx] = None
        else:
            self.expr_type[ctx] = self.variables[ctx.getText()]

    def exitInt(self, ctx: MyParser.IntContext):
        self.expr_type[ctx] = Type.INT

    def exitFloat(self, ctx: MyParser.FloatContext):
        self.expr_type[ctx] = Type.FLOAT

    def exitString(self, ctx: MyParser.StringContext):
        self.expr_type[ctx] = Type.STRING
