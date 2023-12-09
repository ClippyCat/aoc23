import re
with open("p.txt") as file:
	lines = file.readlines()
	lines = [[int(l) for l in line.split()] for line in lines]

def dif(line):
	temp=[]
	for i, l in enumerate(line[1:], start=1):
		diff = line[i-1]-l
		temp.append(diff)
	return line[0]+dif(temp) if any(x!=0 for x in temp) else line[0]

total=0
for i, line in enumerate(lines):
	total+=dif(lines[i])
print(total)