# put your python code here

first_class, second_class, third_class = (int(input()) for _ in range(3))

minimum = (((first_class // 2) + (first_class % 2))
           + ((second_class // 2) + (second_class % 2))
           + ((third_class // 2) + (third_class % 2)))

# minimum = (total // 2) + (total % 2)
print(minimum)
