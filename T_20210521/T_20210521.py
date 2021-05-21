class Calculator:

    def __init__(self, debug_mode=True):
        self.debug = debug_mode

    def run(self):
        a, b, operation = self.get_input()
        result = self.calculate(a, b, operation)
        if self.debug:
            print(result)

    def get_input(self):
        user_input = input("> ").replace(" ", "")
        for operation in ["+", "-", "*", "/"]:
            if operation in user_input:
                splitted = user_input.split(operation)
                return int(splitted[0]), int(splitted[1]), operation
        return None, None, None

    def calculate(self, a, b, operation):
        if operation == "+":
            return self.add(a, b)
        elif operation == "-":
            return self.sub(a, b)
        elif operation == "*":
            return self.mul(a, b)
        elif operation == "/":
            return self.div_3(a, b)

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div_1(self, a, b):
        if b == 0:
            return 0
        return a / b

    def div_2(self, a, b):
        assert b > 0
        return a / b

    def div_3(self, a, b):
        try:
            return a / b, True
        except ZeroDivisionError:
            if self.debug:
                print("Division by Zero not allowed")
            return 0, False


if __name__ == "__main__":
    Calculator().run()
