import re
def get_num(p):
	numbers = re.findall(r'\d+', p.replace(' ', ''))
	return list(map(int, numbers))
p = get_num(open("p.txt").read())

mid=len(p) // 2
dist = p[mid:]
time = p[:mid]

def far(b, r):
	return (r-b)*b
total=1
for i, t in enumerate(time):
#	print(t)
	c=0
	for b in range(1, t+1):
		res=far(b, time[i])
		c+=res > dist[i]
#	print(c)
	total*=c
print(total)