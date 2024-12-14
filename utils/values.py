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
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Int):
            return Int(self.value - other.value)
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Int):
            return Int(self.value * other.value)
        raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, Int):
            if self.value % other.value == 0:
                return Int(self.value // other.value)
            return Float(self.value / other.value)
        raise TypeError()

    def __neg__(self):
        return Int(-self.value)


class Float(Value):
    def __init__(self, value):
        super().__init__(float(value))

    def __add__(self, other):
        if isinstance(other, Float):
            return Float(self.value + other.value)
        raise TypeError()

    def __sub__(self, other):
        if isinstance(other, Float):
            return Float(self.value - other.value)
        raise TypeError()

    def __mul__(self, other):
        if isinstance(other, Float):
            return Float(self.value * other.value)
        raise TypeError()

    def __truediv__(self, other):
        if isinstance(other, Float):
            return Float(self.value / other.value)
        raise TypeError()

    def __neg__(self):
        return Float(-self.value)


class String(Value):
    def __init__(self, value):
        super().__init__(value)


class Vector(Value):
    def __init__(self, value: list):
        super().__init__(value)
        if (
            len(
                {
                    (type(elem), elem.dims if isinstance(elem, Vector) else None)
                    for elem in value
                }
            )
            > 1
        ):
            raise TypeError

        if isinstance(value[0], Vector):
            self.dims = (len(value), *value[0].dims)
        else:
            self.dims = (len(value),)

    def __str__(self):
        return "[" + ", ".join(str(elem) for elem in self.value) + "]"

    def transpose(self):
        if len(self.dims) != 2:
            raise TypeError
        rows = []
        for j in range(self.dims[1]):
            row = [deepcopy(self.value[i].value[j]) for i in range(self.dims[0])]
            rows.append(Vector(row))
        return Vector(rows)
