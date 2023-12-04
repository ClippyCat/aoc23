import re
file_name = 'p.txt'
new_file = 'new.txt'

def remove(file_name, new_file):
	lines = []
	with open(file_name, 'r') as file:
		lines = file.readlines()
		for i, line in enumerate(lines):
			lines[i] = line[line.index(':') +1 :].strip()
	with open(new_file, 'w') as file:
		file.write('\n'.join(lines)) 
remove(file_name, new_file)

def match_list(line):
	win = []
	mine = []
	cards = line.split(' | ')
	win.extend(cards[0].split())
	mine.extend(cards[1].split())
	return set(win) & set(mine)

total=0
with open(file_name, 'r') as file:
	lines = file.readlines()
	for i, line in enumerate(lines):
		match=match_list(line)
		power=len(match)-1

		if (power>=0):
			total+= (2**power)
print(total)