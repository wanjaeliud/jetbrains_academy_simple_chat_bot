# put your python code here

first_hour = int(input())
minutes = int(input())
seconds = int(input())

hrs_seconds = 3600
total_time_1 = (first_hour * hrs_seconds) + (minutes * 60) + seconds

second_hour = int(input())
minute_s = int(input())
second_s = int(input())
total_time_2 = (second_hour * hrs_seconds) + (minute_s * 60) + second_s

time_diff = total_time_2 - total_time_1
print(time_diff)
