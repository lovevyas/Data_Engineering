arr = list(map(int, input("Enter number: ").split()))

def ERP(arr):
    k=0
    f=0
    for i in range(5):    
        k+=arr[i]
        if(arr[i]<35):
            f=1
            break;  
    if(f==1):
        print("FAIL")
    elif(k/5>=75):
        print("DISTINCTION")
    else:
        print("PASS")

result = ERP(arr)
print(result)


# arr=[0]*5
# k=0
# f=0
# for i in range(5):
#     arr[i]=int(input())
#     k+=arr[i]
#     if(arr[i]<35):
#         f=1
#         break;
# if(f==1):
#     print("FAIL")
# elif(k/5>=75):
#     print("DISTINCTION")
# else:
#     print("PASS")





 
