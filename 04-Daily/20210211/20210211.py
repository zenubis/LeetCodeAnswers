# Valid Anagram
# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3636/

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
    # def isAnagram(self, s: str, t: str) -> bool:
    #     ls = len(s)
        
    #     if ls != len(t):
    #         return False
        
    #     lookup = {}
    #     for i in range(ls):
            
    #         if s[i] in lookup:
    #             lookup[s[i]] += 1
    #         else:
    #             lookup[s[i]] = 1
        
    #     try:
    #         for i in range(ls):
    #             lookup[t[i]] -= 1
    #     except KeyError:
    #         return False
            
        
    #     for k in lookup:
    #         if lookup[k] != 0:
    #             return False
            
    #     return True