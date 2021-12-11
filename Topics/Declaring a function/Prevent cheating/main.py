import math

# your code here


def print_error(message):
    print("Don't cheat!")


math.factorial = print_error
# don't delete this line, please
math.factorial(23)
