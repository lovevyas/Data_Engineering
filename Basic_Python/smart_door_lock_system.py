correct_pin = int(input())
f=0
for i in range(3):
    a = int(input())
    if(correct_pin==a):
        f=1

if(f==0):
    print("LOCKED")
else:
    print("ACCESS GRANTED")


