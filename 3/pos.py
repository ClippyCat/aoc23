positions = []
new_pos = [(line_num, int(n.group()), n.start(), n.end() - 1) for n in re.finditer(r'\d+', line)]
positions.extend(new_pos)

for pos in positions:
    print(pos)
