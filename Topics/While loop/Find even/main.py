number = int(input())
num = 0

while num < number:
    num += 1
    # print(num)
    if num % 2 == 0 and num < number:
        print(num)
