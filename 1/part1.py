file_path = 'p.txt'

def combine_chars(line):
	numbers = [char for char in line if char.isdecimal()]
	combined = int(numbers[0] + numbers[-1])
	return combined

sum=0
with open(file_path, 'r') as file:
	for line in file:
		result = combine_chars(line)
		sum+=result
print(sum)