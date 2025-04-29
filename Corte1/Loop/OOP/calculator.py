class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def substraction(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"

if __name__ == "__main__":
    calc = Calculator()

    print(" la suma es: ", calc.add(5, 3))
    print(" la resta es: ", calc.substraction(5, 3))
    print(" el producto: ", calc.multiply(5, 3))
    print(" la razon es: ", calc.divide(5,3) )

