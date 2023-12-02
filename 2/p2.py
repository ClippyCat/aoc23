import re

total = 0
file_name = 'new.txt'

def game_list():
	games = []
	with open(file_name, 'r') as file:
		lines = file.readlines()
		for line in lines:
			texts = line.split()
			cubes = []
			for j in range(1, len(texts), 2):
				cubes.append((int(texts[j-1]), texts[j])) 
			games.append(cubes)
	return games
games = game_list()

for i, game in enumerate(games):
	r=0
	g=0
	b=0
	for cube in game:
		val, col = cube
#		print(val, col)

		if "red" in col and val > r:
			r = val
		if "green" in col and val > g:
			g = val
		if "blue" in col and val > b:
			b = val
	total+= (r*g*b)
print (total)
