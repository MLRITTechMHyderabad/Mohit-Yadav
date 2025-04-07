def calculator(a, b, operator):
    """
    Performs a calculation based on the given operator.
    
    :param a: First number (int/float)
    :param b: Second number (int/float)
    :param operator: String representing an operation (+, -, *, /, %, **)
    :return: Computed result or error message
    """
    try:
        # Ensure inputs are numeric
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Error: Invalid input type. Both operands must be numbers.")
        
        # Dictionary mapping valid operators to functions
        operations = {
            "+": a + b,
            "-": a - b,
            "*": a * b,
            "/": a / b if b != 0 else ZeroDivisionError("Error: Division by zero."),
            "%": a % b if b != 0 else ZeroDivisionError("Error: Division by zero."),
            "": a ** b
        }
        
        if operator not in operations:
            raise ValueError("Error: Unsupported operator.")

        result = operations[operator]

        if isinstance(result, Exception):
            raise result

        return result

    except ZeroDivisionError as e:
        return str(e)
    except ValueError as e:
        return str(e)
    except TypeError as e:
        return str(e)
    except Exception as e:
        return f"Error: An unexpected error occurred - {e}"

# Example Usage:
print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero."
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type. Both operands must be numbers."
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator."
print(calculator(10, 3, ""))   # Should return: 1000 