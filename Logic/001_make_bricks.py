# We want to make a row of bricks that is goal inches long. We have a number of 
# small bricks (1 inch each) and big bricks (5 inches each). Return True if it is 
# possible to make the goal by choosing from the given bricks. 
# This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks 

import math 

def make_bricks(small, big, goal):
	if (goal > (big * 5) + small):
		return False

	neededSmall = goal % 5
	if (small < neededSmall):
		return False

	return True

assert make_bricks(3, 1, 8) is True
assert make_bricks(3, 1, 9) is False
assert make_bricks(3, 2, 10) is True
assert make_bricks(3, 2, 9) is False
assert make_bricks(3, 2, 8) is True
assert make_bricks(6, 1, 11) is True