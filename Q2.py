## import data structures using format below
from data_structures.array_list import ArrayList
from data_structures.bset import BSet

MAX_LENGTH = 200

def find_duplicate_negative_number(input_list: ArrayList) -> int:
	# Idea: Use set (bitset for best efficiency)
	seen = BSet()
	n = len(input_list)
	for i in range(n):
		num = input_list[i]
		idx = get_BSet_index(num)
		
		# Check if seen
		if idx in seen:
			return num
		
		# Else add to set
		seen.add(idx)
	
	# Return -1 by default (shouldn't be the case)
	return -1

# Function to make number appropriate for BSet
def get_BSet_index(el: int) -> int:
    return el * -1

if __name__ == "__main__": # for personal tests
	test = ArrayList(11)
	for i in range(1,10):
		test.append(-1 * i)
	test.append(-4) # dupe
	print(find_duplicate_negative_number(test))
	pass