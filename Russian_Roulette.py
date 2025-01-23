import os
import shutil
import time
from random import randint, seed

# Obtaining a random number of rolls for the gun barrel
t = int(time.time() * 1000)
seed(t)
rolls = randint(50, 80)

# Loading gun based on difficulty chosen ('*' indicates bullet, '' indicates blank)
def load(diff) :
    if diff == 1 :
        return ['*', '', '', '', '', '']        # 1 in 6 chance of death for 'Fun'
    elif diff == 2 :
        return ['*', '*', '*', '', '', '']      # 50-50 for 'Serious'
    else :
        return ['*', '*', '*', '*', '*', '']    # 5 in 6 for 'Death Wish'

# Rolling the list gun n times by list slicing
def roll(gun, n) :
    n = n % len(gun)
    return gun[-n:] + gun[:-n]

# Below is the function that may delete System32. Uncomment at your own risk.
#def death() :
    path = r"C:\Windows\System32"
    try :
        shutil.rmtree(path, ignore_errors=True)
    except :
        print("GUN JAMMED")

# Initialize gun
print("1. Fun\n2. Serious\n3. Death Wish")
h = int(input("Pick difficulty : "))
gun = load(h)
gun = roll(gun, rolls)

# Run an infinite loop that can be exited if:
# - The player chickens out and presses 'o'
# - Only bullets are left in the barrel
# - The player dies
while True :
    f = input("Trigger[x] or Leave[o]? : ")
    
    # Player exits by pressing 'o'
    if f == 'o' :
        time.sleep(3)
        print("...COWARD")
        break
    
    # Fire! First element is popped out of gun
    res = gun.pop(0)
    for i in range(10) :
        print('—', end='')
        time.sleep(0.75)
    print(f'>{res}')

    if res == '*' :
        print("DEAD!")
        #death()        # Uncomment at your own risk
        break
    else :
        print("SAFE!")
        # Check if only bullets are left
        if '' not in gun :
            print("GG, YOU LIVE!")
            break


# Remove comment from lines 22 and 49 if you're feel lucky
# Do it with caution
# shutil.rmtree() might trigger a permission window if it works, so you may live anyway
# Still, do it with caution