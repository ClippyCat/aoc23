import re
from itertools import combinations

with open("p.txt") as file:
	lines = file.readlines()
	lines = [[l for l in line.strip()] for line in lines]

def calc(grid, a, b):
	min_x, max_x = min(a[0],b[0]),max(a[0],b[0])
	min_y, max_y = min(a[1],b[1]),max(a[1],b[1])
	r = [i for i, row in enumerate(grid[min_y:max_y]) if '#' not in row]
	transposed_grid = list(zip(*grid))
	c = [j for j, col in enumerate(transposed_grid[min_x:max_x]) if '#' not in col]
	return abs(a[0]-b[0])+abs(a[1]-b[1])+len(r)+len(c)

def find_dist(grid):
	nodes = [(j,i) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']

	distances = [calc(grid, pos1, pos2) for pos1,pos2 in combinations(nodes,2)]
	return distances

def sum_distances(distances):
	total_distance = 0
	for i in distances:
		for j in distances[i]:
			total_distance += distances[i][j]
	return total_distance

d = find_dist(lines)
print(sum(d))