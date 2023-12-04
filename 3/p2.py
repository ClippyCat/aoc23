import re
import unicodedata

new_file = 'new.txt'

def find_stars():
	with open(new_file, 'r') as file:
		lines = file.readlines()
		stars = []
		for line_num, line in enumerate(lines):
			index = [m.start() for m in re.finditer(r'\*', line)]
			for i in index:
				stars.append((line_num, i))
		return stars

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

def touch_symb(line, num, start, end, i, flines, fline):
	if (i == line) :
		left = fline[start-1]
		right = fline[end+1]
		up = (flines[i-1])[start-1:end+2]
		down = (flines[i + 1])[start - 1:end + 2]
#		down = (flines[i+1])[start-1:end+2]
		return is_symb(left+right+up+down)

positions = find_pos()
stars=find_stars()
fil_pos=[]
with open(new_file, 'r') as file:
	flines = file.readlines()
	for i, fline in enumerate(flines):
		for p, position in enumerate(positions):
			line=position[0]
			num=position[1]
			start=position[2]
			end=position[3]
			if touch_symb(line, num, start, end, i, flines, fline):
				fil_pos.append(position )

#print(fil_pos)
print(stars)

total=0
for s, star in enumerate(stars):
	count = 0
	temp=1
	v = star[0]
	h = star[1]
	#print("star", s)
	#print(v, h)
	for p, position in enumerate(fil_pos):
		line=position[0]
		num=position[1]
		start=position[2]
		end=position[3]
		if (line-1 <= v <= line+1) and (start-1 <= h <= end+1):
			count+=1
			temp*=num
		if count == 2:
			total+=temp
			break
print(total)