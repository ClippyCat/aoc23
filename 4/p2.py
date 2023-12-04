import re

file_name = 'new.txt'

def match_list(line):
	win = []
	mine = []
	#cards = line.split(' | ')
	win.extend(line.split(' | ')[0].split())
	mine.extend(line.split(' | ')[1].split())
	return len(set(win) & set(mine))

def lengths():
	lengths = []
	with open(file_name, 'r') as file:
		lines = file.readlines()
		for line in lines:
			lengths.append(match_list(line))
	return lengths
lengths_list = lengths()
cards=[1 for _ in range(len(lengths_list))]


for i, l in enumerate(lengths_list):
	for copy in range(cards[i]):
		for j in range(1, l+1):
			cards[i+j]+=1
print(sum(cards))
