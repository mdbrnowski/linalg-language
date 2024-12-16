class Type:
    def __eq__(self, other):
        raise TypeError()

    def __lt__(self, other):
        raise TypeError()

    def __le__(self, other):
        raise TypeError()

    def __gt__(self, other):
        raise TypeError()

    def __ge__(self, other):
        raise TypeError()

    def mat_add(self, other):
        raise TypeError()

    def mat_sub(self, other):
        raise TypeError()

    def mat_mul(self, other):
        raise TypeError()

    def mat_truediv(self, other):
        raise TypeError()

    def transpose(self):
        raise TypeError()


class Int(Type):
    def __init__(self, value=None):
        if value is not None:
            self.value = int(value)
        else:
            self.value = None

    def __eq__(self, other):
        if not isinstance(other, Int) and not isinstance(other, Float):
            raise TypeError()

    def __lt__(self, other):
        if not isinstance(other, Int) and not isinstance(other, Float):
            raise TypeError()

    def __le__(self, other):
        if not isinstance(other, Int) and not isinstance(other, Float):
            raise TypeError()

    def __gt__(self, other):
        if not isinstance(other, Int) and not isinstance(other, Float):
            raise TypeError()

    def __ge__(self, other):
        if not isinstance(other, Int) and not isinstance(other, Float):
            raise TypeError()

    def __add__(self, other):
        if isinstance(other, Int):
            if self.value is not None and other.value is not None:
                return Int(self.value + other.value)
            return Int()
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Int):
            if self.value is not None and other.value is not None:
                return Int(self.value - other.value)
            return Int()
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Int):
            if self.value is not None and other.value is not None:
                return Int(self.value * other.value)
            return Int(self.value * other.value)
        raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, Int) or isinstance(other, Float):
            return Float()
        raise TypeError()

    def __neg__(self):
        return Int(-self.value)


class Float(Type):
    def __eq__(self, other):
        if not isinstance(other, Float) and not isinstance(other, Int):
            raise TypeError()

    def __lt__(self, other):
        if not isinstance(other, Float) and not isinstance(other, Int):
            raise TypeError()

    def __le__(self, other):
        if not isinstance(other, Float) and not isinstance(other, Int):
            raise TypeError()

    def __gt__(self, other):
        if not isinstance(other, Float) and not isinstance(other, Int):
            raise TypeError()

    def __ge__(self, other):
        if not isinstance(other, Float) and not isinstance(other, Int):
            raise TypeError()

    def __add__(self, other):
        if isinstance(other, Float) or isinstance(other, Int):
            return Float()
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Float) or isinstance(other, Int):
            return Float()
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Float) or isinstance(other, Int):
            return Float()
        raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, Float) or isinstance(other, Int):
            return Float()
        raise TypeError()

    def __neg__(self):
        return Float()


class String(Type):
    def __eq__(self, other):
        if not isinstance(other, String):
            raise TypeError()

    def __add__(self, other):
        if isinstance(other, String):
            return String()
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Int):
            return String()
        raise TypeError()


class Vector(Type):
    def __init__(self, dims, primitive_type):
        self.dims = dims
        self.primitive_type = primitive_type

    def __eq__(self, other):
        if not same_type(self, other):
            raise TypeError()

    def __lt__(self, other):
        if not same_type(self, other):
            raise TypeError()

    def __le__(self, other):
        if not same_type(self, other):
            raise TypeError()

    def __gt__(self, other):
        if not same_type(self, other):
            raise TypeError()

    def __ge__(self, other):
        if not same_type(self, other):
            raise TypeError()

    def _mat_op(self, other, op):
        new_dims = []
        for self_dim, other_dim in zip(self.dims, other.dims):
            new_dim = self_dim or other_dim
            if new_dim != self_dim or new_dim != other_dim:
                raise TypeError
            new_dims.append(new_dim)
        return Vector(new_dims, op(self.primitive_type, other.primitive_type))

    def mat_add(self, other):
        return self._mat_op(other, lambda x, y: x + y)

    def mat_sub(self, other):
        return self._mat_op(other, lambda x, y: x - y)

    def mat_mul(self, other):
        return self._mat_op(other, lambda x, y: x * y)

    def mat_truediv(self, other):
        return self._mat_op(other, lambda x, y: x / y)

    def transpose(self):
        if len(self.dims) != 2:
            raise TypeError
        return Vector(reversed(self.dims), self.primitive_type)


def same_type(a: Type, b: Type):
    if isinstance(a, Vector):
        return (
            isinstance(b, Vector)
            and a.dims == b.dims
            and same_type(a.primitive_type, b.primitive_type)
        )
    return type(a) is type(b)
