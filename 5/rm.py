import re
file_name = 't.txt'
new_file = 'new.txt'

def remove(file_name, new_file):
	lines = []
	with open(file_name, 'r') as file:
		lines = file.readlines()
		for i, line in enumerate(lines):
			if ':' in line:
				lines[i] = line[line.index(':') +1 :].strip()
	with open(new_file, 'w') as file:
		file.write(''.join(lines))
remove(file_name, new_file)