# PASS_W3
Welcome to week 3's coding activity
Note: you're not allowed to use in-built lists, sets and dictionaries


#### Q1: Valid Parentheses (adapted from [leetcode](https://leetcode.com/problems/valid-parentheses/description/))
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
- `len(input_str) <= 100`

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

*Example 1:*
Input: s = "()", Output: true

*Example 2:*
Input: s = "()[]{}", Output: true

*Example 3:*
Input: s = "(]", Output: false

#### Q2: Find the duplicate negative number (adapted from [leetcode](https://leetcode.com/problems/find-the-duplicate-number/description/))
Given an array of negative integers nums, there is only one repeated number in nums, return this repeated number.
- `len(input_list) <= 200`
- if there are no duplicates, return `-1`

*Example 1:*
Input: nums = [-1,-3,-4,-2,-2], Output: -2

*Example 2:*
Input: nums = [-3,-1,-3,-4,-2], Output: -3

*Example 3:*
Input: nums = [-3,-3,-3,-3,-3], Output: -3

- Extension: can you solve this problem without any collection data structure (i.e. without lists, stacks, sets, queues)
