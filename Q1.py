from data_structures.stack_adt import ArrayStack

MAX_LENGTH = 100

def valid_parentheses(input_str: str):
	st = ArrayStack(MAX_LENGTH)
	for ch in input_str:
		if ch == "(" or ch == "[" or ch == "{":
			st.push(ch)
		elif (st.is_empty() # Not opening bracket to match closing bracket
			or (ch == ")" and st.peek() != "(") # mismatch
			or (ch == "]" and st.peek() != "[") # mismatch
			or (ch == "}" and st.peek() != "{")): # mismatch
			return False
		else: # matching closing bracket
			st.pop()
	return st.is_empty()

if __name__ == "__main__": # for personal tests
	s = "()[]{}"
	print(valid_parentheses(s))