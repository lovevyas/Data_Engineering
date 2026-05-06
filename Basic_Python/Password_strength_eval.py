def passcheck(password):
    for I in password:
        check = 0
        if(len(password)<8):
            print("increase len")
            return False
        if(I.isdigit()):
            check = 1
        if(I.isupper()):
            check = 2
        if(check==2):
            print("all ok")
            return True
    else:
        print("Not upper ",check)
        return False

password = input("Please Enter Password: ")  
if(passcheck(password)):
    print("STRONG")          
else:
    print("WEAK")

        