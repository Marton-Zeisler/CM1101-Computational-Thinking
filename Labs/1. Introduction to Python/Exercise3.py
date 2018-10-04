import random
# 1
player = {}
player["name"] = "Sheldor"
player["health"] = 79
player["ammo"] = 100
del player["ammo"]
print(player)

# 2 -3
player2 = {"name": "Marton", "health" : 100, "experience": 40, "mana": 90, "alive": True, "inventory": ["laptop", "Phone"]}
player2["inventory"].append("Sword")
print(player2)

# 4
for key in player2:
	print(key + " is " + str(player2[key]))

# 5
def print_player(user):
	for key in user:
		print(key + " is " + str(user[key]))
print("\n")
print_player(player2)

# def 6
def compute_experience(damage):
	return random.randrange(0,damage*2)

print(compute_experience(5))

# 7
def take_damage(userPlayer, damage):
	userPlayer["health"] -= damage
	userPlayer["experience"] += compute_experience(damage)
	if userPlayer["health"] <= 0:
		userPlayer["alive"] = False
	return userPlayer

print("\n#7")
print(take_damage(player2, 1))

print("\n\n\n\n\n#8")
# 8
while player2["alive"] == True:
	take_damage(player2, 10)
	print_player(player2)
	print("\n")





