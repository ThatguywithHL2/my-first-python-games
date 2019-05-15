import random

level = "............$......f.......M.....P..."
level = list(level)
hero = "@"


hp = 100
food = 3
gold = 0
hunger = 0
herox=0
def princess():
        """returns True if the player wins
           over the princess, otherwise
           returns False"""
        print (" you have to guess my number")
        print ("but it will be from 1-3")
        p = random.randint(1,3)
        guess= input("your guess?>>>")
        guess= int(guess)
        if guess== p:
            print ("congratulations you heroically guessed my number!")
            print ("have this cookie! see you later")
            return True
        print (" the princess is dissapointed...")
        print ("try again!")
        return False 
        
def fight():
    """returns True if hero vanishes the monster,
       otherwise returns False (monster still alive)"""
    while True:
        print("------Fight!!---------")
        print("you both roll a 6-sided dice")
        d1 = random.randint(1,6)
        print("the monster is rolling a {}".format(d1))
        d2 = random.randint(1,6)
        print("you heroically roll a {}".format(d2))
        # ---result---
        if d1 > d2:
            print("the monster hits you painfully")
            return False
        elif d1 == d2:
            print("it's a draw! you must try again")
        else:
            print("you kick the monster out of the dungeon")
            return True

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
        
        # does player banish the monster?
        if fight():
            # remove the monster from the level
            print("loot!")
            level[herox + dx] = "$"
        else:
            dmg = random.randint(0, 20)
            print("the monster remains, but you got {} damage!".format(dmg))
            hp -= dmg
            dx = 0   # cancel the move
    elif char2 == "P":
        #print("You can not run over a princess")
        if princess():
            level[herox + dx] = "f"
        else:
            print("the princess is still blocking your path")
            dx = 0
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

