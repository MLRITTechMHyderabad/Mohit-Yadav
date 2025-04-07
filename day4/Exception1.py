def calculator(a, b, operator):
    try:
        if type(a) not in [int, float] or type(b) not in [int, float]:
            raise TypeError("Invalid input type")
        elif operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero Error")
            return a / b
        elif operator == "%":
            if b == 0:
                raise ZeroDivisionError("Module by zero Error")
            return a % b
        elif operator == "**":
            return a ** b
        else:
            return "Unsupported operator"

    except ZeroDivisionError as e:
        return e
    except ValueError as e:
        return e
    except TypeError as e:
        return e
    except Exception as e:
        return e

print(calculator(10, 0, "/"))
print(calculator(10, "five", "+"))
print(calculator(10, 5, "$"))