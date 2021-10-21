class calculator:
    def __init__(self,a ,b, typeOfOperation):
        self.a = a
        self.b = b
        self.typeOfOperation = typeOfOperation
        if typeOfOperation == '+':
            print("Result obtained after adding the numbers : ", self.addition())
        elif typeOfOperation == '-':
            print("Result obtained after adding the numbers : ", self.subtraction())
        elif typeOfOperation == '*':
            print("Result obtained after adding the numbers : ", self.multiplication())
        elif typeOfOperation == '/':
            print("Result obtained after adding the numbers : ", self.division())
        else:
            print("Enter a valid type of operation")
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b

a = float(input("Enter the first number\n"))
b = float(input("Enter the second number\n"))
typeOfOperation = input("Enter the type of operation\n")
cal = calculator(a, b, typeOfOperation)
cal
