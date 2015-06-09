# Given a string, return the count of the number of times that a substring length 2 appears 
#  in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 

def last2(str):
	if len(str) < 2:
		return 0

	last = str[-2:]
	count = 0

	for i in range(len(str) - 2):
		sub = str[i : i+2]
		if sub == last:
			count += 1

	return count

assert last2('hixxhi') == 1
assert last2('xaxxaxaxx') == 1
assert last2('axxxaaxx') == 2
