class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero is not allowed."
        return self.a / self.b

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (+, -, *, /): ")
calc = Calculator(a, b)
if operation == '+':
    print("Result:", calc.add())
elif operation == '-':
    print("Result:", calc.subtract())
elif operation == '*':
    print("Result:", calc.multiply())
elif operation == '/':
    print("Result:", calc.divide())
else:
    print("Invalid operation")
