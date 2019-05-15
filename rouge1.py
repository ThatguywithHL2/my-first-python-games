import random

level = "............$......f.......M.....P..."
level = list(level)
hero = "@"


hp = 100
food = 3
gold = 0
hunger = 0
herox=0

def status():
    res = "hero stats: hp: {}  hunger: {} ".format(hp, hunger)
    res += "\ninventory: food: {} gold: {}".format(food, gold)
    return res
    
while hp>0 and hunger < 100:
    for x, char in enumerate(level):
        if x == herox:
            print(hero, end="")
        else:
            print(char, end="")
    print() # new line
    print(status())
    command = input("command? >>>")
    # --- auswertung
    dx = 0
    
    if command == "quit" or command == "exit":
        break 
    elif command == "a":
        dx = -1
        #herox -= 1 # links
        hunger += 1 # 
    if command == "d":
        #herox += 1 # rechts
        dx = 1
        hunger += 1
    if command == "dd":
        #herox += 2 # rechts
        dx = 2
        hunger += 4
    # --- is path free ? ----
    char2 = level[herox + dx]
    if char2 == "M":
        print("A Monster is blocking your path...")
        dx = 0   # cancel the move
    elif char2 == "P":
        print("You can not run over a princess")
        dx = 0   # cancel the move
    else:
        herox += dx  # actually moving 
    if command == "eat" or command == "e":
        if food <= 0:
            print("you have no food to eat!")
        else:
            print("mmmmmmmm, food, tasty")
            food -= 1
            hunger -= 15
    # ---- hero stays on some item ? ----      
    what = level[herox]
    if what == ".":
        pass 
    elif what == "f":
        print("you found a food!")
        food += 1
        level[herox] = "." # remove item
    elif what == "$":
        print ("you found a gold nugget")
        gold += 1
        level[herox] = "." # remove item
    
 
# end of game loop 
print("Game Over")

