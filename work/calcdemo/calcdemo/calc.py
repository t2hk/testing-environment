class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def dif(self):
        return self.a - self.b

    def prod(self):
        return self.a * self.b

    def div(self):
        if self.b == 0:
           raise ZeroDivisionError

        return self.a / self.b

    def exp(self):
        return 0
