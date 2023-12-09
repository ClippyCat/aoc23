import re
with open("p.txt") as file:
	lines = file.readlines()
	lines = [[int(l) for l in line.split()] for line in lines]

def dif(line):
	temp=[]
	for i, l in enumerate(line[1:], start=1):
		diff = l-line[i-1]
		temp.append(diff)
	return line[-1]+dif(temp) if diff != 0 else line[-1]

total=0
for i, line in enumerate(lines):
	total+=dif(line)
print(total)