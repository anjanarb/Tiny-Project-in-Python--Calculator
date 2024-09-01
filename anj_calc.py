def calculator(operation, *args):
    if operation == 'add':
        return sum(args)
    elif operation == 'subtract':
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operation == 'multiply':
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == 'divide':
        result = args[0]
        try:
            for num in args[1:]:
                result /= num
            return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."

# Example usage:
print(calculator('add', 10, 5, 2))        # Output: 17
print(calculator('subtract', 10, 5, 2))   # Output: 3
print(calculator('multiply', 10, 5, 2))   # Output: 100
print(calculator('divide', 10, 5, 2))     # Output: 1.0
