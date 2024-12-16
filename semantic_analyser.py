from copy import deepcopy

from generated.MyParser import MyParser
from generated.MyParserVisitor import MyParserVisitor
from utils.memory import MemoryStack
from utils.types import Int, Float, String, Vector, same_type


class SemanticAnalyser(MyParserVisitor):
    """Checks break and continue statements, variable declarations, types, assignments, etc."""

    def __init__(self):
        self.nested_loop_counter = 0
        self.memory_stack = MemoryStack()
        self.memory_stack.push_memory()

    def visitScopeStatement(self, ctx: MyParser.ScopeStatementContext):
        self.memory_stack.push_memory()
        self.visitChildren(ctx)
        self.memory_stack.pop_memory()

    def visitForLoop(self, ctx: MyParser.ForLoopContext):
        self.visit(ctx.range_())
        variable = ctx.id_().getText()
        if self.memory_stack.get(variable) is None or (
            isinstance(self.memory_stack.get(variable), Int)
        ):
            self.memory_stack.put(variable, Int())
        else:
            ctx.parser.notifyErrorListeners(
                "Incompatible types in an assignment", ctx.getChild(1).getSymbol()
            )
        self.nested_loop_counter += 1
        self.visit(ctx.statement())
        self.nested_loop_counter -= 1

    def visitRange(self, ctx: MyParser.RangeContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        if not isinstance(a, Int) or not isinstance(b, Int):
            ctx.parser.notifyErrorListeners(
                "Range bounds must be integers", ctx.getChild(1).getSymbol()
            )

    def visitWhileLoop(self, ctx: MyParser.WhileLoopContext):
        self.nested_loop_counter += 1
        self.visitChildren(ctx)
        self.nested_loop_counter -= 1

    def visitComparison(self, ctx: MyParser.ComparisonContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        try:
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
        except TypeError:
            ctx.parser.notifyErrorListeners(
                "Incompatible types in a comparison", ctx.getChild(1).getSymbol()
            )

    def visitSimpleAssignment(self, ctx: MyParser.SimpleAssignmentContext):
        if ctx.id_():  # a = 1
            variable = ctx.id_().getText()
            new_type = self.visit(ctx.expression())
            if self.memory_stack.get(variable) is None or (
                same_type(self.memory_stack.get(variable), new_type)
            ):
                self.memory_stack.put(variable, new_type)
            else:
                ctx.parser.notifyErrorListeners(
                    "Incompatible types in an assignment", ctx.getChild(1).getSymbol()
                )
        else:  ## a[0] = 1
            pass  # todo

    def visitCompoundAssignment(self, ctx: MyParser.CompoundAssignmentContext):
        return self.visitChildren(ctx)  # todo

    def visitBinaryExpression(self, ctx: MyParser.BinaryExpressionContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))
        try:
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
        except TypeError:
            ctx.parser.notifyErrorListeners(
                "Incompatible types in a binary operation",
                ctx.getChild(1).getSymbol(),
            )

    def visitParenthesesExpression(self, ctx: MyParser.ParenthesesExpressionContext):
        return self.visit(ctx.expression())

    def visitTransposeExpression(self, ctx: MyParser.TransposeExpressionContext):
        try:
            return self.visit(ctx.expression()).transpose()
        except TypeError:
            ctx.parser.notifyErrorListeners(
                "Transpose operator can only be applied to matrices",
                ctx.getChild(1).getSymbol(),
            )

    def visitMinusExpression(self, ctx: MyParser.MinusExpressionContext):
        try:
            return -self.visit(ctx.expression())
        except TypeError:
            ctx.parser.notifyErrorListeners(
                "Unary minus can be applied only to integers or floats",
                ctx.MINUS().getSymbol(),
            )

    def visitSpecialMatrixFunction(self, ctx: MyParser.SpecialMatrixFunctionContext):
        fname = ctx.getChild(0).symbol.type
        if fname == MyParser.EYE:
            dim = self.visit(ctx.expression(0))
            if not isinstance(dim, Int):
                ctx.parser.notifyErrorListeners(
                    "Matrix dimentions must be integers", ctx.getChild(0).getSymbol()
                )
                return
            return Vector((dim.value, dim.value), Int())
        else:
            dims = [
                self.visit(ctx.expression(i))
                for i in range(ctx.getChildCount() // 2 - 1)
            ]
            if not all(isinstance(dim, Int) for dim in dims):
                ctx.parser.notifyErrorListeners(
                    "Matrix dimentions must be integers", ctx.getChild(0).getSymbol()
                )  # todo: add more specific symbol
                return
            return Vector(
                tuple(dim.value for dim in dims), Int()
            )  # todo: return Int(0) or Int(1)

    def visitBreak(self, ctx: MyParser.BreakContext):
        if self.nested_loop_counter == 0:
            ctx.parser.notifyErrorListeners(
                "Break statement outside of loop", ctx.BREAK().getSymbol()
            )

    def visitContinue(self, ctx: MyParser.ContinueContext):
        if self.nested_loop_counter == 0:
            ctx.parser.notifyErrorListeners(
                "Continue statement outside of loop", ctx.CONTINUE().getSymbol()
            )

    def visitVector(self, ctx: MyParser.VectorContext):
        elements = [
            self.visit(ctx.expression(i)) for i in range(ctx.getChildCount() // 2)
        ]
        for i in range(1, len(elements)):
            if not same_type(elements[i], elements[i - 1]):
                wrong_token = ctx.COMMA(i) or ctx.CLOSE_BRACKET_SQUARE()
                ctx.parser.notifyErrorListeners(
                    "Inconsistent types in a vector", wrong_token.getSymbol()
                )
                return None
        elem = elements[0]
        if isinstance(elem, Int):
            elem.value = None
        if isinstance(elem, Vector):
            return Vector((len(elements), *elem.dims), elem.primitive_type)
        else:
            return Vector((len(elements),), elem)

    def visitElementReference(self, ctx: MyParser.ElementReferenceContext):
        indices = [
            self.visit(ctx.expression(i)) for i in range(ctx.getChildCount() // 2 - 1)
        ]
        if not all(isinstance(index, Int) for index in indices):
            ctx.parser.notifyErrorListeners(
                "Indices must be integers", ctx.OPEN_BRACKET_SQUARE().getSymbol()
            )
            return
        result = deepcopy(self.visit(ctx.id_()))
        if not isinstance(result, Vector):
            ctx.parser.notifyErrorListeners(
                "Indexing can only be applied to vectors",
                ctx.OPEN_BRACKET_SQUARE().getSymbol(),
            )
            return
        for idx in indices:
            if not isinstance(result, Vector):
                ctx.parser.notifyErrorListeners(
                    "Too many indices", ctx.OPEN_BRACKET_SQUARE().getSymbol()
                )
                return
            if (
                idx.value is not None
                and result.dims[0] is not None
                and idx.value >= result.dims[0]
            ):
                ctx.parser.notifyErrorListeners(
                    "Index out of bounds", ctx.OPEN_BRACKET_SQUARE().getSymbol()
                )
                return
            result.dims = result.dims[1:]
            if len(result.dims) == 0:
                result = result.primitive_type
        return result

    def visitId(self, ctx: MyParser.IdContext):
        result = self.memory_stack.get(ctx.getText())
        if result is not None:
            return result
        else:
            ctx.parser.notifyErrorListeners(
                f"Variable {ctx.getText()} not declared", ctx.ID().getSymbol()
            )

    def visitInt(self, ctx: MyParser.IntContext):
        return Int(ctx.getText())

    def visitFloat(self, ctx: MyParser.FloatContext):
        return Float()

    def visitString(self, ctx: MyParser.StringContext):
        return String()
