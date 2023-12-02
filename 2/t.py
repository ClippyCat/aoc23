import re
file_name = 'p.txt'
new_file = 'new.txt'


def contain(line, string_list):
	for s in string_list:
		if s in line:
			return True
	return False
string_list = ["15", "16", "17", "18", "19", "20", "13 red", "14 red", "14 green"]


def remove(file_name, new_file):
	lines = []
	with open(file_name, 'r') as file:
		lines = file.readlines()
		for i, line in enumerate(lines):
			lines[i] = line[line.index(':') + 1:].strip()
	with open(new_file, 'w') as file:
		file.write('\n'.join(lines)) 

def sum_up(file_name):
	sum=0
	with open(file_name, 'r') as file:
		for i, line in enumerate(file, start=1):
			if not contain(line, string_list):
				sum+=i
	print(sum)

remove(file_name, new_file)
sum_up(new_file)