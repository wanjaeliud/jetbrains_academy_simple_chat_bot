angle_h = int(input())
angle_b = int(input())
angle_s = int(input())
total = angle_s + angle_b + angle_h
angle = 180
if total == angle:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")
