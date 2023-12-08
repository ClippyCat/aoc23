import re
from collections import Counter

'''
def change_rank(r, j):
	while j>0:
		if r == 6:
			r=7
		elif r == 5:
			r=7
		elif r == 4:
			r = 6
		elif r == 3:
			r = 5
		elif r == 2:
			r = 4
		else:
			r = 2
		j-=1
	return r
'''

def highest(cards):
#	if cards[0] == 1 and cards[1] == 1:
#		print("CARDS: ", cards)
	counts = Counter(cards)
	occurrences = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
	highest_card = occurrences[0][0]
	rank = sorted(counts.values(), reverse=True)
	if highest_card == 1:
		if rank == [5]:
			highest_card = 14
		else:
			highest_card = occurrences[1][0]
#	print("HI: ", highest_card)
	return highest_card

def check_hand(cards):
	hi = highest(cards)
	no_joker_cards = [hi if x == 1 else x for x in cards]
	counts = Counter(no_joker_cards)
	rank = sorted(counts.values(), reverse=True)
	r=0
	if rank == [5]:
		r = 7  # Five of a Kind
	elif rank == [4, 1]:
		r = 6  # Four of a Kind
	elif rank == [3, 2]:
		r = 5  # Full House
	elif 3 in rank:
		r = 4  # Three of a Kind
	elif rank.count(2) == 2:
		r = 3  # Two Pair
	elif 2 in rank:
		r = 2  # One Pair
	else:
		r = 1  # High Card
#	r=change_rank(r, cards.count(1))
	return r

#check_hand(hand)[1]
def replace_hand(hand):
	new_hand=[]
	for i, h in enumerate(hand):
		if h.isdigit():
			new_hand.append(int(h)) 	  	
		elif h in ['t', 'T']:
			new_hand.append(10)
		elif h in ['j', 'J']:
			new_hand.append(1)
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
#check_hand(p[i])[1]
	hands_list.append((replace_hand(p[i]), int(p[i+1])))

results = []
for hand in hands_list:
	result = (check_hand(hand[0]), hand[0], hand[1])
#	#print(result)
	results.append(result)


#results.sort(key=lambda x: (x[0]))
results.sort(key=lambda x: (x[0], x[1]))

'''
start=1
end=1
for i, r in enumerate(results):
	if r[1] < results[i+1][1]:
		end=i+1
		results[start:end].sort(key=lambda x: move_11(x[1]))
		start=end
'''



total=0
for i, result in enumerate(results):
	total+=result[2]*(i+1)
#	print(f"Hand: {result[1]}, Rank: {i+1}")
print(total)