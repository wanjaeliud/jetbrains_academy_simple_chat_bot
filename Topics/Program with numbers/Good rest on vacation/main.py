# put your python code here
days_spent, food_cost_day, flight_cost, hotel_cost_night = (int(input())
                                                            for _ in range(4))
total_food_cost = days_spent * food_cost_day
flight = flight_cost * 2
total_hotel_cost = (days_spent - 1) * hotel_cost_night

total_vacation_cost = total_food_cost + flight + total_hotel_cost
print(total_vacation_cost)
