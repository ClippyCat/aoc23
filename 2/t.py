import re
file_name = 'p.txt'
new_file = 'new.txt'

def remove(file_name, new_file):
	lines = []
	with open(file_name, 'r') as file:
		lines = file.readlines()
		for i, line in enumerate(lines):
			lines[i] = line[line.index(':') +1 :].strip()
			lines[i] = lines[i].replace(',', '')
			lines[i] = lines[i].replace(';', '')
	with open(new_file, 'w') as file:
		file.write('\n'.join(lines)) 
remove(file_name, new_file)


def game_list():
	games = []
	with open(new_file, 'r') as file:
		lines = file.readlines()
		for line in lines:
			texts = line.split()
			cubes = []
			for j in range(1, len(texts), 2):
				cubes.append((int(texts[j-1]), texts[j])) 
			games.append(cubes)
	return games
games = game_list()
r=12
g=13
b=14


def total():
	total = 0
	for i, game in enumerate(games, start=1):
		num = i
		for cube in game:
			val, col = cube
			if ("red" in col and val > r) or ("green" in col and val > g) or ("blue" in col and val > b):
				num = 0
#		print(num)
		total+= num
	return total

print (total())
