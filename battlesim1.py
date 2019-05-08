import random

# battle simulator
leo = 88
yj = 100
# damage ~ 11

print("battle between LEO and YJ")
while True:
	print("hitpoints Leo: {}    hitpoints YJ: {}".format(leo, yj))
	dmg = random.randint(0,6)
	print("leo attacking and makes {} damage".format(dmg))
	#yj = yj - dmg
	yj -= dmg
	if yj <= 0:
		print("yj dies, leo wins!")
		break
	print("yj has {} hitpoints left".format(yj))
	dmg = random.randint(0,3)
	print("yj attacking and makes {} damage".format(dmg))
	leo-= dmg
	if leo <= 0:
		print("leo dies, yj wins!")
		break
	print("leo has {} hitpoints left".format(leo))
print("game over")
