# Given a three-digit integer (i.e., an integer from 100 to 999).
# Find the sum of its digits and print the result.

number = int(input())
result = 0
num = number
while num != 0:
    remainder = num % 10
    result += remainder
    num = num // 10
print(result)
