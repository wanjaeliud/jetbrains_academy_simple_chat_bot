# Ask the user about parameters of a rectangular parallel piped
# (3 integers representing the length, width, and height)
# and print the sum of edge lengths, its total surface area, and the volume.
# Sum of lengths of all edges:
# s=4(a+b+c)

# Surface area:
# S=2(ab+bc+ac)

# Volume:
# V=abc

length, width, height = (int(input()) for _ in range(3))

sum_of_lengths = 4 * (length + width + height)
surface_area = 2 * ((length * width) + (width * height) + (length * height))
volume = length * width * height

print(f"{sum_of_lengths}\n{surface_area}\n{volume}")
