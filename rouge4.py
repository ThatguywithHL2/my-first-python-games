import random

        

class Monster():
    number = 0
    zoo = {}
    
    def __init__(self, x):
        self.number = Monster.number
        Monster.number += 1
        Monster.zoo[self.number] = self
        self.x = x
        self.hp = random.randint(10,50)
        self.attack = 0.6 # = 60 % 
        self.defense = 0.3 # = 30 %
        self.damage = 5
        self.char = "M"
        self.name = random.choice(("Bob","Alice", "Carl"))
        
    def introduce(self):
        print("i am a {} and i have the number {}".format(self.__class__.__name__, self.number))
        print("i stand around at position {} in the dungeon".format(self.x))
        
    def ai(self):
        """returns a dx of where the monster wants to go"""
        return random.choice((-1,0,0,0,1))

class Princess(Monster):
    
    def __init__(self, x):
        Monster.__init__(self, x)
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
       
class Hero(Monster):
    
    def __init__(self, x):
        Monster.__init__(self,x)
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
        
    def status(self):
        res = "hero stats: hp: {}  hunger: {} ".format(self.hp, self.hunger)
        res += "\ninventory: food: {} gold: {}".format(self.food, self.gold)
        return res
    
    
        




print("____________")
print ("HERO QUEST")
print("_____________")
print("-.-.-.-.-.-.-.-.-.-.-.-")
level = "............$......f....M...M.....P...."
level = list(level)


## ---- create my little monsters for my dungeon ---

hero = Hero(0) # place a hero instance at x position 0

for xpos, char in enumerate(level):
    if char == "M":
        Monster(x=xpos)
        level[xpos] = "." # make a normal floor
    elif char == "P":
        Princess(x=xpos)
        level[xpos] = "." # make a normal floor

for m in Monster.zoo.values():
    m.introduce()
    



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
     
# ====== main game loop ========

while hero.hp>0 and hero.hunger < 100:
    for x, char in enumerate(level):
        # graphic engine
        for m in Monster.zoo.values():
            if x == m.x and m.hp > 0: 
                print(m.char, end="")
                break
        else:
            print(char, end="")
    print() # new line
    print(hero.status())
    command = input("command? >>>")
    # --- auswertung
    dx = 0
    
    if command == "quit" or command == "exit":
        break 
    elif command == "a":
        dx = -1
        #herox -= 1 # links
        hero.hunger += 1 # 
    if command == "d":
        #herox += 1 # rechts
        dx = 1
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
    # --- is path free ? ----
    char2 = level[hero.x + dx]
    for m in Monster.zoo.values():
        # ignore the hero!
        if m.number == hero.number:
            continue
        if m.hp <= 0:
            continue # ignore dead monsters
        if m.x == hero.x + dx:
            # someone is blocking heros path!
            
            if m.__class__.__name__ == "Monster":
                print("A Monster is blocking your path...")
        
                # does player banish the monster?
                fight(hero, m)
                # remove the monster from the level
                if hero.hp > 0:
                     print("loot!")
                     level[hero.x + dx] = "$"
                dx = 0 # block heros movement
            
            elif m.__class__.__name__ == "Princess":
            
                #print("You can not run over a princess")
                if m.talk():
                    level[hero.x + dx] = "f"
                else:
                    print("the princess is still blocking your path")
                dx = 0 # block heros movement
                
    
    hero.x += dx  # actually moving 
    if command == "eat" or command == "e":
        if hero.food <= 0:
            print("you have no food to eat!")
        else:
            print("mmmmmmmm, food, tasty")
            hero.food -= 1
            hero.hunger -= 15
    # ---- hero stays on some item ? ----      
    what = level[hero.x]
    if what == ".":
        pass 
    elif what == "f":
        print("you found a food!")
        hero.food += 1
        level[hero.x] = "." # remove item
    elif what == "$":
        print ("you found a gold nugget")
        hero.gold += 1
        level[hero.x] = "." # remove item
    
 
# end of game loop 
print("Game Over")

