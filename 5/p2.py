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

def seeds():
	lines = []
	with open(new_file, 'r') as file:
		lines = file.readlines()
	return [int(s) for s in lines[0].split()]
seeds_list = seeds()
#print(seeds_list)

def split_maps():
	lines = []
	with open(new_file, 'r') as file:
		lines = file.readlines()[1:]
	return ''.join(lines).split('\n\n')
maps=split_maps()

def line_to_nums(line):
	nums = line.split()
	return (int(nums[0]), int(nums[1]), int(nums[2]))

def sec_to_num(section):
	return [line_to_nums(line) for line in section.split("\n")]

data = list(map(sec_to_num, maps))
#print(data)

def calc(data, v):
	for deez in data:
		for l in deez:
			dest=l[0]
			src=l[1]
			leng=l[2]
			if (src<= v < src+leng):
				v= dest+v-src
				break
	return v

result=[]

for i in range(0, len(seeds_list), 2):
	start_seed = seeds_list[i]
	length = seeds_list[i + 1]
	for s in range(start_seed, start_seed + length):
		result.append(calc(data, s))
print(min(result))
