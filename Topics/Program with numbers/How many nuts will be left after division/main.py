# N squirrels found K nuts and decided to divide them equally.
# Find how many nuts will be left after each of the squirrels takes the equal amount of nuts.
#     Input data format
# There are two positive integers N and K, neither of them are greater than 10000

n_squirrels = int(input())
k_nuts = int(input())
nuts_left = k_nuts % n_squirrels
print(nuts_left)
