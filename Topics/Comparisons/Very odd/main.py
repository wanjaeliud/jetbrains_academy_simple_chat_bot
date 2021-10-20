number, divisor = (int(input()) for _ in range(2))

odd = (number // divisor) % 2 != 0
print(odd)
