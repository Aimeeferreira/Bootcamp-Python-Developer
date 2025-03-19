def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def display_result(a, b, function):
    result = function(a, b)
    print(f"The result of the calculation is {result}")


display_result(10, 10, add)  # The result of the calculation is 20
display_result(10, 10, sub)  # The result of the calculation is 0


op = add
print(op(1,23))
