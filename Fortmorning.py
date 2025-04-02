import random
import time
running = True

while running:
    monster_val = random.randint(0, 4269)

    choice = input("Want to enter building?(y/n)")

    

    if monster_val % 6 == 0 and choice == "y":
        print("The peeler found you!!")
    else:
        print("You are safe.....for now....")
