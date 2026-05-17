TANK_CAPACITY = 1000

num_of_min = int(input())

inflows = list(map(int, input().split()))

if len(inflows) != num_of_min:
    raise ValueError("Number of inflow should be equals to number of minutes")

vol_of_water = 0

for minute, inflow in enumerate(inflows, start=1):
    vol_of_water += inflow
    if vol_of_water > TANK_CAPACITY:
        print(minute)
        break

