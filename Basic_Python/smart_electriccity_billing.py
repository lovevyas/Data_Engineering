def calculate(units):
    cost = 0
    penalty = 0
    if(units<=100):
        cost = units*3
    elif(units<=200):        
        cost = 300+((units-100)*5)
          
    else:
        cost = 800 + (units-200)*8        
        if(units>300):
            cost += (cost*0.1)
    return cost
                
    

units = int(input("Amount of unit used: "))
total_units = units
cost = calculate(units)
print(f"Total Bill: {cost}")
