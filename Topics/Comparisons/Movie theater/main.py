number_of_halls, capacity, viewers = (int(input()) for _ in range(3))
viewers_per_day = viewers <= (number_of_halls * capacity)
print(viewers_per_day)
