import re
from collections import Counter

def check_hand(cards):
	counts = Counter(cards)
	occurrences = sorted(counts.values(), reverse=True)
	if occurrences == [5]:
		return 7  # Five of a Kind
	elif occurrences == [4, 1]:
		return 6  # Four of a Kind
	elif occurrences == [3, 2]:
		return 5  # Full House
	elif 3 in occurrences:
		return 4  # Three of a Kind
	elif occurrences.count(2) == 2:
		return 3  # Two Pair
	elif 2 in occurrences:
		return 2  # One Pair
	else:
		return 1  # High Card


def replace_hand(hand):
	new_hand=[]
	for i, h in enumerate(hand):
		if h.isdigit():
			new_hand.append(int(h))
		elif h in ['t', 'T']:
			new_hand.append(10)
		elif h in ['j', 'J']:
			new_hand.append(11)
		elif h in ['q', 'Q']:
			new_hand.append(12)
		elif h in ['k', 'K']:
			new_hand.append(13)
		elif h in ['a', 'A']:
			new_hand.append(14)
	return new_hand

with open("p.txt") as file:
	p = file.read().split()

hands_list = []
for i in range(0, len(p), 2):
	hands_list.append((replace_hand(p[i]), int(p[i+1])))

results = []
for hand in hands_list:
	result = (check_hand(hand[0]), hand[0], hand[1])
	#print(result)
	results.append(result)

results.sort(key=lambda x: (x[0], x[1]))


total=0
for i, result in enumerate(results):
	total+=result[2]*(i+1)
#	print(f"Hand: {result[1]}, Rank: {i+1}")
print(total)