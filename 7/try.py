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

with open("t.txt") as file:
	p = file.read().strip().split()

hands_list = []
for i in range(0, len(p), 2):
	hands_list.append((p[i], p[i+1]))

results = []
for hand in hands_list:
	result = (check_hand(hand), hand)
	print(result)
	results.append(result)

results.sort(key=lambda x: (x[0], x[1][0]), reverse=True)

#for result in results:
#	print(f"Hand: {result[1]}, Rank: {result[0]}")

#for hand in hands_list:
#print(check_hand(hands_list[]))