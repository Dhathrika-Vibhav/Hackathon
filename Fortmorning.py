import random
import time
running = True

while running:
    monster_val = random.randint(0, 4269)

    choice = input("Want to enter building?(y/n)")

    

    if monster_val % 6 == 0 and choice == "y":
        print("aye!! sulla get over here")
    else:
        print("il get u bagude wait da")
