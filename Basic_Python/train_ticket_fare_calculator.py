distance = int(input("Enter distance: "))
age = int(input("Enter Age: "))

def fare_cal(distance,age):
    fare = distance*2
    if(age>=60):
        fare = fare*0.7
    elif(age<12):
        fare = fare*(0.5)
    return round(fare)

print(fare_cal(distance,age))

    