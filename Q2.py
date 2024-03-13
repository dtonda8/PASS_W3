from data_structures.array_list import ArrayList
from data_structures.bset import BSet

MAX_LENGTH = 200

def find_duplicate_negative_number(input_list: ArrayList):
	s = BSet(MAX_LENGTH)
	for i in range(len(input_list)):
		if -1 * input_list[i] in s:
			return input_list[i]
		s.add(-1 * input_list[i])
	return -1

if __name__ == "__main__": # for personal tests
	test = ArrayList(11)
	for i in range(1,10):
		test.append(-1 * i)
		test.append(-4)
	print(find_duplicate_negative_number(test))
	pass