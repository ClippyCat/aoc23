import re
import unicodedata

file_name = 'p.txt'
new_file = 'new.txt'

def boarder(file_name, new_file):
	lines = []
	with open(file_name, 'r') as file:
		lines = file.readlines()
		lines = ["b" + line.strip() + "b" for line in lines]
		with open(new_file, 'w') as file:
			file.write('b' * (len(lines[0])) + '\n')
			file.write('\n'.join(lines))
			file.write('\n' + 'b' * (1+len(lines[0])))
boarder(file_name, new_file)

def find_pos():
	with open(new_file, 'r') as file:
		lines = file.readlines()
		positions = []
		new_pos=[]
		for line_num, line in enumerate(lines):
			new_pos = [(line_num, int(n.group()), n.start(), n.end()-1) for n in re.finditer(r'\d+', line)]
			positions.extend(new_pos)
	return positions

def is_symb(str):
	for c in str:
		if (unicodedata.category(c).startswith('S') or unicodedata.category(c).startswith('P')) and c != '.':
			return True
	return False

def touch_symb(position, i, flines, fline):
	line=position[0]
	num=position[1]
	start=position[2]
	end=position[3]
	if (i == line) :
		left = fline[start-1]
		right = fline[end+1]
		up = (flines[i-1])[start-1:end+2]
		down = (flines[i+1])[start-1:end+2]
		print("DATA: ", left+right+up+down)
		print("is_symbol: ", is_symb(left+right+up+down))
		return is_symb(left+right+up+down)

positions = find_pos()
print(positions)
sum=0
with open(new_file, 'r') as file:
	flines = file.readlines()
	for i, fline in enumerate(flines):
		for p, position in enumerate(positions):
			if touch_symb(position, i, flines, fline):
				print(position[1])
				sum+=position[1]
print("SUM: ", sum)
