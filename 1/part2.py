file_path = 'p.txt'
file_new = 'new.txt'
def new_file(content):
	char_map = {
		'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e',
		'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'
	}
	for char, replacement in char_map.items():
		content = content.replace(char, replacement)
	return content

def combine_chars(line):
	numbers = [char for char in line if char.isdecimal()]
	combined = int(numbers[0] + numbers[-1])
	return combined

total_sum = 0

with open(file_path, 'r') as file:
	content = file.read()
	modified_content = new_file(content)

with open(file_new, 'w') as file:
	file.write(modified_content)

with open(file_new, 'r') as file:
	for line in file:
		result = combine_chars(line)
		total_sum += result

print(total_sum)
