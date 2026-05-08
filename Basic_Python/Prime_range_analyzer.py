import math
A = int(input())
B = int(input())

def noPrime(A,B):
    count = 0
    for i in range(A,B+1):   
        if i < 2: # 0 and 1 are not prime
            continue  
        1   
        flag=0
        for j in range(2,math.isqrt(i)+1):
            if(i%j==0):
                flag=1
                break;
                
        if(flag==0):
            count+=1  

    return count      

count = noPrime(A,B)
print(count)
        




        