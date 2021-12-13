sleep_hoursA = int(input())
excess_hoursB = int(input())
ann_sleepH = int(input())

if ann_sleepH > excess_hoursB:
    print("Excess")
else:
    if ann_sleepH < sleep_hoursA:
        print("Deficiency")
    else:
        print("Normal")
