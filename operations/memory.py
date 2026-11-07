class Memory:
    def __init__(self):
        self.value = 0.0

    def m_plus(self, x):
        self.value += x
        return self.value

    def m_minus(self, x):
        self.value -= x
        return self.value

    def mr(self):
        return self.value

    def mc(self):
        self.value = 0.0
        return 0.0
