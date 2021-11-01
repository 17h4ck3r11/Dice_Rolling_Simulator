# Dice rolling simulator 


import random
print(
'''
               /* RULES FOR THE GAME */

1. You have only 10 moves to score maximum points.
2. At the end of 10 moves, your final score will be shown.
3. You have to press y , to roll the Dice.
4. If 6 shown in Dice, three times continuously, you will be out!
5. Your final score is equal to the sum of all numbers shown in the Dice.
6. If you press any key, other than y, you will lose!
'''
)
count = 0
total_score = 0

while count < 10:
    count += 1

    character = input("Press y to roll the dice : ")

    roll = random.randint(1, 6)

    roll_list = []
    roll_list.append(roll)

    if roll_list[-3:] == [6, 6, 6]:
        print("Your Score is",total_score)
        break
    
    total_score += roll

    if character =='y' or character == 'Y':
        if roll == 1:
            print(" ____________ ")
            print("|            |")
            print("|            |")
            print("|     O      |")
            print("|            |")
            print("|____________|") 
        elif roll == 2:
            print(" ____________ ")
            print("|            |")
            print("|            |")
            print("|  O      O  |")
            print("|            |")
            print("|____________|") 
        elif roll == 3:
            print(" ____________ ")
            print("|            |")
            print("|            |")
            print("| O   O   O  |")
            print("|            |")
            print("|____________|")      
        elif roll == 4:
            print(" ____________ ")
            print("|            |")
            print("| O        O |")
            print("|            |")
            print("| O        O |")
            print("|____________|")                        
        elif roll == 5:
            print(" ____________ ")
            print("|            |")
            print("| O        O |")
            print("|      O     |")
            print("| O        O |")
            print("|____________|")                 
        else:
            print(" ____________ ")
            print("|            |")
            print("| O        O |")
            print("| O        O |")
            print("| O        O |")
            print("|____________|")         

    else:
        break
    
if count == 10:
    print("Your Score is",total_score)