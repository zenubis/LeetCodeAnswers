# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3610/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:
    # 1 <= s.length <= 104
    # s consists of parentheses only '()[]{}'.



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in range(len(s)):
            if s[x] == '(' or s[x] == '[' or s[x] == '{':
                stack.append(s[x])
            elif s[x] == ')':
                if not self.PopAndCheck(stack, '('):
                    return False
            elif s[x] == ']':
                if not self.PopAndCheck(stack, '['):
                    return False
            elif s[x] == '}':
                if not self.PopAndCheck(stack, '{'):
                    return False
            
        return len(stack) == 0
    
    def PopAndCheck(self, stack, char):
        try:
            ch = stack.pop()
            return char == ch
        except IndexError as e:
            return False
            
