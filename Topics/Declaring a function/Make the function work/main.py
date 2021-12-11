def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder == 0:
        return x
    return x + (5 - remainder)

# def closest_higher_mod_5(x):
#     if x != 0:
#         remainder = x % 5
#         if remainder == 0:
#             return x
#         elif 0 < remainder <= 2:
#             return x - remainder
#         else:
#             return x + (5 - remainder)
#     else:
#         return 0
