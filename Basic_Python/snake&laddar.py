import random


def roll_dice():
    return random.randint(1,6)
def check_options():
    return random.randint(0,2)


def play(player):    
    position = 0
    count =  0
    while position <100:
        count+=1
        dice = roll_dice()
        option = check_options()
        if option == 0:
            pass
        elif option == 1:
            position += dice
            if(position>100):
                position -= dice
        elif option == 2:
            position -= dice
            if position < 0:
                position =0
        print(f"Dice: {dice} -->> Position: {position}")
        if(position==100):
            print("You won!", player)
            print("Total moves:",count)
    
play("Love vyas")
            
        
    

    
    