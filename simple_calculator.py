class Calculator:
 def branch_add(self, a, b):
    return a + b

 def subtract(self, x, y):
    return x - y

 def multiply(self, a, b):
    return a * b
 
if __name__ == "__main__":
 calc = Calculator()
 print("Addition: ", calc.branch_add(10, 5))
 print("Subtraction: ", calc.subtract(10, 5))
 print("Multiplication: ", calc.multiply(10, 5))