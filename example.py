a = 1
b = 5

def add_numbers(x, y):
    return x + y
def subtract_numbers(x, y):
    return x - y
def multiply_numbers(x, y):
    return x * y
def divide_numbers(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

answer_add = add_numbers(a, b)
answer_subtract = subtract_numbers(a, b)
answer_multiply = multiply_numbers(a, b)
try:
    answer_divide = divide_numbers(a, b)
except ValueError as e:
    answer_divide = str(e)

print(f"Addition: {answer_add}")
print(f"Subtraction: {answer_subtract}")
print(f"Multiplication: {answer_multiply}")
print(f"Division: {answer_divide}")