class Value:
    def __init__(self, value):
        self.value = value

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
