import random

# battle simulator, slightly improved, horizontal health bars  
leo = 30
yj = 70
# damage ~ 11

def strike(attacker, defender, hp_d, max_dmg):
    dmg = random.randint(0, max_dmg)
    print("{} is attacking {} and inflicts {} damage".format(attacker, defender, dmg))
    hp_d -= dmg
    print("{} has {} hp left".format(defender, hp_d))
    if hp_d <= 0:
        print("{} dies, {} wins".format(defender, attacker))
    return hp_d

print("battle between LEO and YJ")


combat_round = 1
while True:
    print("combat round", combat_round)
    command = input("press enter to continue, q and enter to quit")
    if command == "q":
        break
    #print("hitpoints Leo: {}    hitpoints YJ: {}".format(leo, yj))
    print("hp leo:", leo * "+")
    print("hp yj :",yj * "#")
    
    yj = strike("leo", "yj", yj, 6) 
    if yj <= 0:
        break
    leo = strike("yj", "leo", leo, 3)
    if leo <= 0:
        break   
    combat_round += 1
print("game over")
