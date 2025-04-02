import random
import time
running = True

while running:
    player_pos_y = 0
    player_pos_x = 0
    
    peeler_val = random.randint(0, 426)

    venomelon_val = random.randint(0, 100000000)

    movement = input("Where do you want to go??(W/A/S/D)")

    if movement == "W":
        
