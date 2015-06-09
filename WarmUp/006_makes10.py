# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10. 

def makes10(a, b):
	return a + b == 10 or a == 10 or b == 10;  


assert makes10(9, 10) is True
assert makes10(9, 9) is False
assert makes10(1, 9) is True