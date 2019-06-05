import random

    

class Monster():
    number = 0
    zoo = {}
    
    def __init__(self, x,y, z):
        self.number = Monster.number
        Monster.number += 1
        Monster.zoo[self.number] = self
        self.x = x
        self.y = y
        self.z = z
        self.hp = random.randint(10,50)
        self.attack = 0.6 # = 60 %
        self.defense = 0.3 # = 30 %
        self.damage = 5
        self.char = "M"
        self.name = random.choice(("Bob","Alice", "Carl"))
    
    def introduce(self):
        print("i am a {} and i have the number {}".format(self.__class__.__name__, self.number))
        print("i stand around at position x:{} y:{} z:{}in the dungeon\n".format(self.x, self.y, self.z))
    
    def ai(self):
        """returns a dx of where the monster wants to go"""
        return random.choice((-1,0,0,0,1))

class Princess(Monster):
    
    def __init__(self, x,y,z):
        Monster.__init__(self, x,y,z)
        self.char = "P"
        self.name = "Tanja"
   
    def talk(self):
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
            self.hp = 0
            return True
        print (" the princess is dissapointed...")
        print ("try again!")
        return False  

class Box(Monster):
    
    def __init__(self, x,y,z):
        Monster.__init__(self,x,y,z)
        self.hp = 100
        self.char = "o"
 
class Door(Monster): 
    
    def __init__(self, x,y,z):
        Monster.__init__(self,x,y,z)
        self.hp = 100
        self.attack = 0 # = 60 %
        self.defense = 0 # = 0 %
        self.damage = 0
        self.char = "D"
        self.name = random.choice(("Tür","Door", "Gate"))    
        self.lock_quality= random.randint(1,10)   
        
class Trader(Monster):
    
    def __init_(self, x,y,z):
        Monster.__init__(self,x,y,z)
        self.hp = 100
        self.attack = 0 # = 60 %
        self.defense = 0 # = 0 %
        self.damage = 0
        self.char = "D"
        self.name = random.choice(("Tür","Door", "Gate"))       
        
class Midboss(Monster):
    
    def __init__(self, x,y,z):
        Monster.__init__(self,x,y,z)
        self.gold = random.randint(1000,3000)
        self.skill = random.randint(1000,3000)
        self.betting = random.randint(1,6) 
        self.char = "§"         
        
     
class Hero(Monster):
    
    def __init__(self, x,y,z):
        Monster.__init__(self,x,y,z)
        self.hp = 100
        self.char = "@"
        self.name = "arnie"
        self.hunger=0
        self.gold=0
        self.food=0
        self.hunger = 0
        self.attack = 0.85
        self.defense = 0.50
        self.damage = 10
        self.lockpicking = 2
        self.charisma = 1
            
    def status(self):
        res = "hero stats: hp: {}  hunger: {} ".format(self.hp, self.hunger)
        res += "\ninventory: food: {} gold: {}".format(self.food, self.gold)
        res += " charisma:{} lockpicking:{}".format(self.charisma, self.lockpicking)
        return res
 
    




print("____________")
print ("HERO QUEST")
print("_____________")
print("-.-.-.-.-.-.-.-.-.-.-.-")
d1 = """
########################################################
#@......#.$.#....#....M...............##.D.........#####
#<......####.#....#...##...M...........MMD.........P####
#.....#.............f.#...............#####D############
####D######D##############..###############D############
#.......###.###########......f.############.############
#.......#.........f##......§.....##....MM...$f.#########
#...€...#..########################...MM...$f....fffff##
#.......#.........................D...MM...$f...########
########################################################
"""

d2="""
########################################################
#.............##......####...........f...#....$f$#######
#>.f$f........##..........#M##...........###############
#...f............####........##..........#...........###
##################################.$.....D...........###
                               #.........#...........###
                               #########################
"""
d3="""
###############################################
#............................................##
#..............#.............................##
#..............#..........B..................##
#..............#..##.........................##
#..............#...#................###########
#..............###B##...............D........##
#...................:...............#........##
###############################################
"""#
level = []
#----------------- generate levels ----------
for z,d in enumerate((d1,d2,d3)):
    mylevel = []
    for y, line in enumerate(d.splitlines()):
        row = []
        for x, char in enumerate(line):
            if char == "@":
                hero = Hero(x,y,z)
                row.append(".")
            elif char == "M":
                Monster(x,y,z)
                row.append(".")
            elif char == "P":
                Princess(x,y,z)
                row.append(".")
            elif char == "B":
                Box(x,y,z)
                row.append(".")
            elif char=="D":
                Door(x,y,z)
                row.append(".")
            elif char=="§":
                Midboss(x,y,z)
                row.append(".")  
            else:
                row.append(char)
        mylevel.append(row)
    level.append(mylevel)

#level = list(level)


## ---- create my little monsters for my dungeon ---

#hero = Hero(0) # place a hero instance at x position 0

for m in Monster.zoo.values():
    m.introduce()

def open_door(human,door):
    print("hero heroically tries to open a closed door!")
    d1 = random.randint(1,5)
    d2 = random.randint(1,4)
    print("hero rolls: {} + {} = {}".format(d1, d2, d1+d2))
    print("hero lockpicking: {}".format(human.lockpicking))
    print("door balse lock quality (difficulty): {}".format(door.lock_quality))
    print("door level factor {}".format(human.z +1))
    skill = d1+d2+ human.lockpicking
    difficulty = door.lock_quality * (human.z+1)
    
    print("door difficulty = {} * {} = {}".format(door.lock_quality, human.z+1, difficulty)) 
    
    print("your skill: {}".format(skill))
    
    print("lockpicking is dice 1+ dice 2 if the dice is grater than Lock then it will open for you")
    if skill > difficulty:
        print("hurra! door is open")
        door.hp = 0
        return True
    # else
    print("this door is beyond your skill")
    return False
    
def gamble(human, midboss):
    if human.gold <1:
        print(" haha! you fool! did you really think you could gamble for free?")
        print(" dont show yourself here again without some money!")     
        return    

def fight(attacker, defender):
    battleround = 0
    while attacker.hp > 0 and defender.hp > 0:
        battleround += 1
        print("round {}".format(battleround))
        print("==== Strike ====")
        strike(attacker, defender)
        if defender.hp > 0:
            print("=== counter-strike ====")
            strike(defender, attacker)
    
        
def strike(attacker, defender):
    """returns True if hero vanishes the monster,
    otherwise returns False (monster still alive)"""
    d1 = random.random()
    d2 = random.random() # 0...1
    d3 = random.randint(1,6)
    print("strike of {} the {} vs. {} the {}".format(
        attacker.name, attacker.__class__.__name__,
        defender.name, defender.__class__.__name__))
    print(" attack ok? ")
    print("attacker rolls {}, attack value is {}".format(d1, attacker.attack))
    if d1 < attacker.attack:
        print("attack sucessfull")
    else:
        print("attack fumbled")
        return
    print("defender can block?")
    print("defender rolls {}, defend value is {}".format(d2, defender.defense))
    if d2 < defender.defense:
        print("defense sucessfull! Attack is blocked")
        return
    print("defender could not negate the attack")
    print("base damage {} + roll {} = {}".format(attacker.damage, d3, attacker.damage + d3))
    totaldam = d3 + attacker.damage
    print("defender suffers {} damage".format(totaldam))
    defender.hp -= totaldam
    if defender.hp <= 0:
        print("Victory for {}".format(attacker.name))
    command = input("press enter for next action")


    
def push(pusher, box):
        """returns False if the Box is not pushable,
           otherwise returns the dungeon tile where the
           box is now standing and changes the x,y values
           of both pusher and box"""
        # self....the box
        # pusher ... usually the hero
        dx, dy = 0, 0
        if pusher.x == box.x:
            if pusher.y == box.y-1:
                dy = 1 # pushing south
            if pusher.y == box.y + 1:
                dy = -1 # pushing north
        elif pusher.y == box.y:
            if pusher.x == box.x - 1:
                dx = 1 # pushing east
            if pusher.x == box.x + 1:
                dx = -1 # pushing west
        else:
            print("pushing not possible, distance too big")
            return False
        new_tile = level[z][box.y+dy][box.x+dx]
        if new_tile == "#":
            print("pushing is blocked by wall")
            return False
        else:
            print("you heroically push the box around")
            # new coordinates for box
            box.x += dx
            box.y += dy
            # new coordinates for pusher
            pusher.x += dx
            pusher.y += dy 
            return new_tile

 
# ====== main game loop ========

z = 0

while hero.hp>0 and hero.hunger < 100:
    for y, line in enumerate(level[z]):
        for x, char in enumerate(level[z][y]):
            # graphic engine
            for m in Monster.zoo.values():
                if m.hp > 0 and m.z==z and m.y==y and m.x==x:
                    print(m.char, end="")
                    break
            else:
                print(char, end="")
        print() # new line
    print(hero.status())
    command = input("command? >>>")
    # --- auswertung
    dx = 0
    dy = 0
    if command == "quit" or command == "exit":
        break
    if command == "down":
        z += 1
        hero.z += 1
    if command == "up":
        z-= 1
        hero.z -= 1
    elif command == "a":
        dx = -1
        #herox -= 1 # links
        hero.hunger += 1 #
    if command == "d":
        #herox += 1 # rechts
        dx = 1
        hero.hunger += 1
    if command == "w":
        dy = -1 # up
        hero.hunger += 1
    if command == "s":
        dy = 1 # down
        hero.hunger += 1
    if command == "dd":
        #herox += 2 # rechts
        dx = 2
        hero.hunger += 4
    if command == "speed!":
        #herox += 8 # rechts
        # cost 5 gold.
        if hero.gold >= 5:
            dx= 8
            hero.gold -= 5
            hero.hunger += 20
        else:
            print("not enough gold! you need 5 gold for this cheat")
    if command == "TECH":
        #herox += 32 # rechts
        dx= 32
    if command == "MILLIONARE":
        hero.gold += 100 
    if command == "credits":
        print("-.-.-.-.-.-.-.-.-.-.-.-")
        print ("made by Leo Larsson")  
        print("-.-.-.-.-.-.-.-.-.-.-.-")
    if command == "eat" or command == "e":
           if hero.food <= 0:
               print("you have no food to eat!")
           else:
               print("mmmmmmmm, food, tasty")
               hero.food -= 1
               hero.hunger -= 15
    # --- is path free ? ----
    char2 = level[z][hero.y +dy][hero.x + dx]
    # box blocking ?
    #for m in Monster.zoo.values():
    #    if m.__class__.__name__ == "Box":
    #        if m.z == hero.z:
    #            if hero.x + dx == m.x and hero.y + dy == m.y:
    #                new_tile = push(hero, m)
    #                dx, dy = 0, 0
    #                if new_tile == ":":
    #                    print("Hurra, box is good placed")
    #                break
    # monster blocking ?
    for m in Monster.zoo.values():
        # ignore the hero!
        if m.number == hero.number:
            continue
        # ignore monser in wrong level
        if m.z != z :
            continue 
        # ignore dead monsters         
        if m.hp <= 0:
            continue  
        if m.x == hero.x + dx and m.y == hero.y + dy:              # someone is blocking heros path!
            if m.__class__.__name__ == "Box":
                new_tile = push(hero, m)
                dx, dy = 0, 0
                if new_tile == ":":
                    print("Hurra, box is good placed")
                break
            elif m.__class__.__name__ == "Door":
                if open_door(hero, m):
                    print("the open door disappears")
                else:
                    print("the closed door is still blocking your path")
                dx = 0
                dy = 0
                break   
            elif m.__class__.__name__ == "Monster":
                print("A Monster is blocking your path...")
                # does player banish the monster?
                fight(hero, m)
                # remove the monster from the level
                if hero.hp > 0:
                    print("loot!")
                    level[z][hero.y + dy][hero.x + dx] = "$"
                dx = 0 # block heros movement
                dy = 0
            elif m.__class__.__name__== "Midboss":
	            print("do you want to gamble with me? ill bet youll loose!")
	            dx=0
	            dy=0
	            break 			
               
            elif m.__class__.__name__ == "Princess":
                #print("You can not run over a princes            if m.talk():
                level[z][hero.y + dy][hero.x + dx] = "f"
            else:                    
                print("Error! the program does not know who is blocking your path")
                dx = 0 # block heros movement
                dy = 0
    #-------- wall blocking ?
    if char2 == "#":
         print("ouch, you run against a wall")
         dx = 0
         dy = 0
    hero.x += dx  # actually moving
    hero.y += dy
    # ---- hero stays on some item ? ----    
    what = level[z][hero.y][hero.x]
    if what == ".":
        pass
    elif what == "f":
           print("you found a food!")
           hero.food += 1
           level[z][hero.y][hero.x] = "." # remove item
    elif what == "$":
           print ("you found a gold nugget")
           hero.gold += 1
           level[z][hero.y][hero.x] = "." # remove item
# end of game loop
print("Game Over")
