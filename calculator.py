class calculator:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

obj = calculator(94 , 10)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.div())
        
