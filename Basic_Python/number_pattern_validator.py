num = input("Enter the number: ")

flag = 0
for i in range(len(num)-1):
    if int(num[i])>int(num[i+1]):
        flag=1
        break;

if(flag==0):
    print("YES")
else:
    print("NO")
