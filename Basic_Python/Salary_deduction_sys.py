salary = int(input("Enter the salary: "))
late_days = int(input("No. of Late days: "))
absent_days = int(input("No. of Absent days: "))

def Sds(salary, ld, abd ):
    deduct = 0
    if(ld>5):
        deduct = 0.05
    elif(ld>10):
        deduct = 0.10
    if abd > 2:
        deduct += 0.05
    return int(salary*(1-deduct))

print(Sds(salary, late_days, absent_days))