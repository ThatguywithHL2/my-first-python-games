import random

# battle simulator, slightly improved
leo = 88
yj = 100
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
while True:
    print("hitpoints Leo: {}    hitpoints YJ: {}".format(leo, yj))
    yj = strike("leo", "yj", yj, 6) 
    if yj <= 0:
        break
    leo = strike("yj", "leo", leo, 3)
    if leo <= 0:
        break   
print("game over")
