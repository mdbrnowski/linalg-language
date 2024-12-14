from copy import deepcopy


class Value:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        try:
            return self.value == other.value
        except TypeError:
            raise TypeError()

    def __lt__(self, other):
        try:
            return self.value < other.value
        except TypeError:
            raise TypeError()

    def __le__(self, other):
        try:
            return self.value <= other.value
        except TypeError:
            raise TypeError()

    def __gt__(self, other):
        try:
            return self.value > other.value
        except TypeError:
            raise TypeError()

    def __ge__(self, other):
        try:
            return self.value >= other.value
        except TypeError:
            raise TypeError()


class Int(Value):
    def __init__(self, value):
        super().__init__(int(value))

    def __add__(self, other):
        if isinstance(other, Int):
            return Int(self.value + other.value)
        elif isinstance(other, Float):
            return Float(self.value + other.value)
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Int):
            return Int(self.value - other.value)
        elif isinstance(other, Float):
            return Float(self.value - other.value)
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Int):
            return Int(self.value * other.value)
        elif isinstance(other, Float):
            return Float(self.value * other.value)
        raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, Int):
            return Float(self.value / other.value)
        elif isinstance(other, Float):
            return Float(self.value / other.value)
        raise TypeError()

    def __neg__(self):
        return Int(-self.value)


class Float(Value):
    def __init__(self, value):
        super().__init__(float(value))

    def __add__(self, other):
        if isinstance(other, Float) or isinstance(other, Int):
            return Float(self.value + other.value)
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Float) or isinstance(other, Int):
            return Float(self.value - other.value)
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Float) or isinstance(other, Int):
            return Float(self.value * other.value)
        raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, Float) or isinstance(other, Int):
            return Float(self.value / other.value)
        raise TypeError()

    def __neg__(self):
        return Float(-self.value)


class String(Value):
    def __init__(self, value):
        super().__init__(value)

    def __add__(self, other):
        if isinstance(other, String):
            return String(self.value + other.value)
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Int):
            return String(self.value * other.value)
        raise TypeError()


class Vector(Value):
    def __init__(self, value: list):
        super().__init__(value)
        if (
            len(
                {
                    (
                        (elem.dims, elem.primitive_type)
                        if isinstance(elem, Vector)
                        else type(elem)
                    )
                    for elem in value
                }
            )
            > 1
        ):
            raise TypeError

        if isinstance(value[0], Vector):
            self.dims = (len(value), *value[0].dims)
            self.primitive_type = value[0].primitive_type
        else:
            self.dims = (len(value),)
            self.primitive_type = type(value[0])

    def __str__(self):
        return "[" + ", ".join(str(elem) for elem in self.value) + "]"

    def _mat_op(self, other, op):
        if isinstance(other, Vector):
            rows = []
            for elem, other_elem in zip(self.value, other.value):
                if isinstance(elem, Vector):
                    rows.append(elem._mat_op(other_elem, op))
                else:
                    rows.append(op(elem, other_elem))
            return Vector(rows)
        raise TypeError()

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
        rows = []
        for j in range(self.dims[1]):
            row = [deepcopy(self.value[i].value[j]) for i in range(self.dims[0])]
            rows.append(Vector(row))
        return Vector(rows)
