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
    
    def __init__(self, x,y,z):
        Monster.__init__(self,x,y,z)
        self.hp = 100
        self.attack = 0 # = 60 %
        self.defense = 0 # = 0 %
        self.damage = 0
        self.char = "€"
        self.name = random.choice(("Trader","Shopkeeper"))       
        
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
 
    
picture1="""
 /$$   /$$ /$$$$$$$$ /$$$$$$$   /$$$$$$           
| $$  | $$| $$_____/| $$__  $$ /$$__  $$          
| $$  | $$| $$      | $$  \ $$| $$  \ $$          
| $$$$$$$$| $$$$$   | $$$$$$$/| $$  | $$          
| $$__  $$| $$__/   | $$__  $$| $$  | $$          
| $$  | $$| $$      | $$  \ $$| $$  | $$          
| $$  | $$| $$$$$$$$| $$  | $$|  $$$$$$/          
|__/  |__/|________/|__/  |__/ \______/           
                                                  
                                                  
  /$$$$$$  /$$   /$$ /$$$$$$$$  /$$$$$$  /$$$$$$$$
 /$$__  $$| $$  | $$| $$_____/ /$$__  $$|__  $$__/
| $$  \ $$| $$  | $$| $$      | $$  \__/   | $$   
| $$  | $$| $$  | $$| $$$$$   |  $$$$$$    | $$   
| $$  | $$| $$  | $$| $$__/    \____  $$   | $$   
| $$/$$ $$| $$  | $$| $$       /$$  \ $$   | $$   
|  $$$$$$/|  $$$$$$/| $$$$$$$$|  $$$$$$/   | $$   
 \____ $$$ \______/ |________/ \______/    |__/   
      \__/                                        
                          
"""
healthpicture1="""
 _____ _____ ___________   
|  __ \  _  |  _  |  _  \ 
| |  \/ | | | | | | | | | 
| | __| | | | | | | | | | 
| |_\ \ \_/ | \_/ / |/ /  
 \____/\___/ \___/|___/   
"""
healthpicture2="""
       _
      | |   
  ___ | | __
 / _ \| |/ /
| (_) |   < 
 \___/|_|\_\
"""

healthpicture3="""
                    _ _                 
                   | (_)                
 _ __ ___   ___  __| |_ _   _ _ __ ___  
| '_ ` _ \ / _ \/ _` | | | | | '_ ` _ \ 
| | | | | |  __/ (_| | | |_| | | | | | |
|_| |_| |_|\___|\__,_|_|\__,_|_| |_| |_|
"""

healthpicture4="""
 _                    _               _ _           
| |                  | |             | (_)          
| |__   __ _ _ __ ___| |_   _    __ _| |___   _____ 
| '_ \ / _` | '__/ _ \ | | | |  / _` | | \ \ / / _ \
| |_) | (_| | | |  __/ | |_| | | (_| | | |\ V /  __/
|_.__/ \__,_|_|  \___|_|\__, |  \__,_|_|_| \_/ \___|
"""
healthpicture5="""
               _ _    _                                             
              | | |  (_)                                            
__      ____ _| | | ___ _ __   __ _    ___ ___  _ __ _ __  ___  ___ 
\ \ /\ / / _` | | |/ / | '_ \ / _` |  / __/ _ \| '__| '_ \/ __|/ _ \
 \ V  V / (_| | |   <| | | | | (_| | | (_| (_) | |  | |_) \__ \  __/
  \_/\_/ \__,_|_|_|\_\_|_| |_|\__, |  \___\___/|_|  | .__/|___/\___|
                               __/ |                | |             
                              |___/                 |_|        
"""

hiddenimage1="""
      __      _______ _   _ 
     /\ \    / / ____| \ | |
    /  \ \  / / |  __|  \| |
   / /\ \ \/ /| | |_ | . ` |
  / ____ \  / | |__| | |\  |
 /_/    \_\/   \_____|_| \_|
"""

helptext = """
@............you, the hero
D............Door
M............Monster
#............wall
P............Princess

]............helpful sign
"""

signs = {0: ["welcome to the dungeon",
                 "you need a key for this door",
                 "you are useless"],
         1: ["congrats, you made it into the next level"]
           }


print(picture1)

input("press enter to start")
d1 = """
########################################################
#@......#.$..#..#....M..........].....##.D.........#####
#<......####.#....#...##...M...........MMD.........P####
#...].#.............f.#...............#####D############
####D######D##############.]###############D############
#.......###.###########......f.############.############
#.......#.........f##......§.....##....MM...$f.#########
#...€...#..########################...MM...$f....fffff##
#.......#.........................D...MM...$f...########
########################################################




Level 1 

Main cave         


"""

d2="""
########################################################
#.............##......####.......]...f...#....$f$#######
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
            elif char=="€":
                Trader(x,y,z)
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
    

def sign_rank(level,hx, hy, hz):
    rank = -1
    for y, line in enumerate(level[hz]):
        for x, char in enumerate(line):
            if char == "]":
                rank += 1
            if x == hx and y == hy:
                return rank
    return None
    

def read_sign(z, hero, level):
    x = hero.x
    y = hero.y
    li = signs[z]
    # rank of sign in this level:
    rank = sign_rank(level, x,y,z)
    if rank is None:
        print("sign not found!!", x,y,z)
    else:
        print(signs[z][rank])
            
            
            
   
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

def trade(hero,trader):
    print ("you start trading")
    # TODO trading 

def flirt(hero,girl):
    print("======================== FLIRT-SCREEN ==================")
    print("you see a most gorgous princess. Your hormons drive you crazy")
    print("she looks at you, expecting YOU to say something clever")
    print("give her your best line!")
    pickupline = input("(type and press ENTER) >>>")
    #print("insert text here....")
    print("summoning all your charisma, you look her straight into the eyes")
    print("and snarl:", pickupline)
    print("================== RESULT ==========================")
    z = random.randint(1,3)
    if z == 1:
        print ("very good you have succesfully impressed her")
        hero.hp += 3
        hero.hunger -= 5
    elif z== 2:
         print ("you try to speak to her but she fully ignores you and it crushes your self confidence")
         hero.hp = 0
    
    elif z==3:  
        print ("you barely get her attention and she compliments your shoes")
        hero.hp += 1
        hero.gold -= 50
        print ("while you look at your ugly shoes she snatches your wallet and steals 50 gold")
    #### in any case 
    girl.hp = 0
    print("press Enter to continue playing")
    input(">>>")    

# ====== main game loop ========

z = 0

#-----DUNGEON ENGINE-----
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
    if command in ["help", "?", "what", "tutorial"]:
        print(helptext)
        input("press ENTER to continue")
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
        if m.x == hero.x + dx and m.y == hero.y + dy:
            # someone is blocking heros path!
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
                break
            elif m.__class__.__name__== "Midboss":
                print("do you want to gamble with me? ill bet youll loose!")
                dx=0
                dy=0
                break           
               
            elif m.__class__.__name__ == "Princess":
                #print("You can not run over a princes            if m.talk():
                m.hp = 0
                flirt(hero,m)
                print("the princess likes you, gives you some food and dissappears")
                level[z][hero.y + dy][hero.x + dx] = "f"
                dx, dy = 0,0
                break
                
            elif m.__class__.__name__== "Trader":
                dx, dy= 0,0
                trade(hero, m)
                break
                
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
    elif what == "]":
        # a sign
        print("you see a sign")
        print("it reads:")
        read_sign(z, hero, level)
        input("press enter to continue")
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
