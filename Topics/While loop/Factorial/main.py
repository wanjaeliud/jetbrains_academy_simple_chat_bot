num = int(input())

factorial = 1  # declare and initialize factorial variable to one

# check if the number is negative ,positive or zero
# if num < 0:
#     print("Factorial does not defined for negative integer")
# elif num == 0:
#     print("1")
# else:
while num > 0:
    factorial *= num
    num -= 1
print(factorial)
