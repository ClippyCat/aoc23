import re
with open("p.txt") as file:
	lines = file.readlines()
	grid = [list(line.strip()) for line in lines]
#print(lines)

pipes = {
	"|": ["n", "s"],
	"-": ["w", "e"],
	"L": ["n", "e"],
	"J": ["n", "w"],
	"7": ["s", "w"],
	"F": ["s", "e"],
	'S': ["n", "s", "w", "e"],
}

directions = {
	"n": (-1, 0, "s"),
	"s": (1, 0, "n"),
	"w": (0, -1, "e"),
	"e": (0, 1, "w"),
}

def find_start(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if 'S' in grid[i][j]:
				return [i, j]
start=find_start(grid)
#print(start)


visited ={}
#search = [(start, 0)]
search = [(tuple(start), 0)]  # Convert start to a tuple
while len(search) > 0:
	cur, dist = search.pop(0)
	if cur not in visited:
		visited[cur] = dist
		i, j = cur
		for direction in pipes[grid[i][j]]:
			di, dj, opposite = directions[direction]
			new = (i + di, j + dj)
			if i + di < 0 or i + di >= len(grid) or j + dj < 0 or j + dj >= len(grid[i + di]):
				continue
			target = grid[i + di][j + dj]
			if target not in pipes:
				continue
			target_directions = pipes[target]
			if opposite in target_directions:
				search.append((new, dist + 1))


def get_type(i, j):
	can_reach = []
	for direction in directions:
		di, dj, opposite = directions[direction]
		if i + di < 0 or i + di >= len(grid) or j + dj < 0 or j + dj >= len(grid[i + di]) or (i + di, j + dj) not in visited:
			continue
		targ = grid[i + di][j + dj]
		targ_directions = pipes[targ]
		can_reach.append(direction)
	for type in pipes:
		if len(can_reach) == len(pipes[type]):
			if all([direction in pipes[type] for direction in can_reach]):
				return type

grid[start[0]][start[1]] = get_type(start[0], start[1])
for i in range(len(grid)):
	north = 0
	for j in range(len(grid[i])):
		p = grid[i][j]
		if (i,j) in visited:
			pipe_directions = pipes[p]
			if "n" in pipe_directions:
				north += 1
			continue
		if north % 2 == 0:
			grid[i][j] = "O" 
		else:
			grid[i][j] = "I"

print("\n".join(["".join(line) for line in grid]).count("I"))
