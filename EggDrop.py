# Provided that you have two eggs, find out the how many steps are required to get the floor that breaks the egg
# Given: Two eggs and hidden floor number that breaks the egg

def egg_threshold(total_floor, egg_break_floor):
    '''
    Algorithm in action: Binary traversal and Linear tranversal
    Time Complexity: 
    '''
    steps = 0
    ground_floor = 0

    # First Egg | Broke test with binary triversal
    while True:
        steps += 1
        drop_floor = (ground_floor+total_floor)//2 # Mid Floor
        print(f"Step {steps} at floor {drop_floor}")

        if egg_break_floor == drop_floor:
            break
        elif drop_floor > egg_break_floor: # Egg broke: Drop floor is greater than egg_break_floor
            print(f"------------Egg 01 broke at floor {drop_floor}-------------\n")
            drop_floor = ground_floor
            break
        else:
            ground_floor = drop_floor

    # Second Egg | Linear triversal for the second egg
    while drop_floor != egg_break_floor:
        steps += 1
        drop_floor += 1
        print(f"Step {steps} at floor {drop_floor}")
    print(f"------------Egg 02 broke at floor {drop_floor}-------------\n")

    return steps

total_floor, break_floor = 30, 18
print("Egg Break Floor estimated in {} steps".format(egg_threshold(total_floor, break_floor)))