def oodEng(value):
    arr = [0.05,0.1,0.2]
    if(value>=5000):        
        value = value*(1-arr[2])
    elif(value>=3000):
        value = value*(1-arr[1])
    elif(value>=1000):
        value = value*(1-arr[0])
    return value

amount = int(input())
print(oodEng(amount))
    

