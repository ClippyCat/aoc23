from math import lcm
import re

with open("p.txt") as file:
	p = re.sub(r'[^a-zA-Z\s]', '', file.read()).split()

lr = p[0]
print(lr)

network = []
for i in range(1, len(p), 3):
	network.append((p[i], p[i + 1], p[i + 2]))

def find_name(next_node):
	for i, node in enumerate(network):
		if node[0] == next_node:
			return node

def step(l, d):
	next_node=0
	if d == 'L':
		next_node = l[1]
	elif d == 'R':
		next_node = l[2]
	return find_name(next_node)


ass=list(filter(lambda x: x[0].endswith('A'), network))

def walk(next_node):
	steps = 0
	i = 0
	while not next_node[0].endswith('Z'):
		next_node = step(next_node, lr[i])
		steps += 1
		i += 1
		if i == len(lr):
			i = 0
	return steps

steps = list(map(walk, ass))


print(lcm(*steps))