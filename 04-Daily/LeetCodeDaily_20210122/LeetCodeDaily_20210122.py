# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3613/
#
# Two strings are considered close if you can attain one from the other using the following operations:
#     Operation 1: Swap any two existing characters.
#         For example, abcde -> aecdb
#     Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#         For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

# Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

# Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

# Example 3:
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

# Example 4:
# Input: word1 = "cabbba", word2 = "aabbss"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any amount of operations.

# Constraints:
#     1 <= word1.length, word2.length <= 10^5
#     word1 and word2 contain only lowercase English letters.

import collections

class Solution:
    def closeStrings(self, word1:str, word2:str) -> bool:
        w1_freq = collections.Counter(word1)
        w2_freq = collections.Counter(word2)

        #if different set of letters then fail
        for w in w1_freq:
            if not w in w2_freq:
                return False
        
        return sorted(w1_freq.values()) == sorted(w2_freq.values())






def checkAnswer(s:Solution, w1:str, w2:str, ans:bool):
    output = s.closeStrings(w1, w2)
    if output != ans:
        print("Wrong answer")
        print(output)
        print(ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    checkAnswer(s, "abc", "bca", True)
    checkAnswer(s, "a", "aa", False)
    checkAnswer(s, "cabbba", "abbccc", True)
    checkAnswer(s, "cabbba", "aabbss", False)
    