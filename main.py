from operations import ALL_OPERATIONS, Memory


class Calculator:
    def __init__(self, root):
        self.root = root
        self.expr = ""
        self.memory = Memory()
        self.operations = ALL_OPERATIONS
