from .values import Value


class Memory:
    def __init__(self):
        self.variables: dict[str, Value] = {}

    def has_variable(self, name: str) -> bool:
        return name in self.variables

    def get(self, name: str) -> Value:
        return self.variables[name]

    def put(self, name: str, value: Value):
        self.variables[name] = value


class MemoryStack:
    def __init__(self):
        self.stack: list[Memory] = []

    def get(self, name: str) -> Value:
        for memory in self.stack:
            if memory.has_variable(name):
                return memory.get(name)

    def put(self, name: str, value: Value):
        for memory in self.stack:
            if memory.has_variable(name):
                memory.put(name, value)
                return
        self.stack[-1].put(name, value)

    def push_memory(self):
        self.stack.append(Memory())

    def pop_memory(self):
        self.stack.pop()
