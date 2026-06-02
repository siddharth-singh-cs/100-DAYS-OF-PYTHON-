print("welcome to the treasure isand your mission is to find the treasure ")
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
dir=input('you are in a open land would you go "left" or "right"')
if dir=="left" or dir=="Left":
    print("a wild animal killed you! game over")



if dir=="right" or dir=="Right":
    second_step=input('you arrive at a shore and see an island infront of you but to reach that you need to cross the river would you like to "swin" or "wait"?')
if second_step=="swin":
    print("you got eaten by crocodiles!!")

if second_step=="wait":
        print('you arrive in a palace there are three doors infront of you "red","yellow" and "blue"\n')
        door=input("which door would you like to go in?")
        if door=="red":
            print("you got eaten by a lion! game over")
        elif door=="blue":
            print("you were killed by bandits")
        else:
            print("you win 456 million dollars")
        

          



