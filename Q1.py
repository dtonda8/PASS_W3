## import data structures using format below
from data_structures.array_list import ArrayList
from data_structures.stack_adt import ArrayStack

MAX_LENGTH = 100
OPEN_BRACKETS = "({["
CLOSE_BRACKETS = ")}]"

def valid_parentheses(input_str: str) -> bool:
    # Stack for open brackets
    open_bracket_st = ArrayStack(MAX_LENGTH)
    for bracket in input_str:
        if bracket in OPEN_BRACKETS:
            open_bracket_st.push(bracket)
            
        elif bracket in CLOSE_BRACKETS:
            # check if open bracket does not match closing bracket, if so, return False (invalid parentheses)
            if (len(open_bracket_st) == 0 or # not matching bracket at all
                OPEN_BRACKETS.index(open_bracket_st.pop()) != CLOSE_BRACKETS.index(bracket)):
                return False
    
    # If no more open brackets remain, return true
    return len(open_bracket_st) == 0

if __name__ == "__main__": # for personal tests
	s = "()[]{}"
	print(valid_parentheses(s))
	pass