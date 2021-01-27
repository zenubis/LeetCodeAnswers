# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3618/

# Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

# Example 1:
# Input: n = 1
# Output: 1
# Explanation: "1" in binary corresponds to the decimal value 1. 

# Example 2:
# Input: n = 3
# Output: 27
# Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
# After concatenating them, we have "11011", which corresponds to the decimal value 27.

# Example 3:
# Input: n = 12
# Output: 505379714
# Explanation: The concatenation results in "1101110010111011110001001101010111100".
# The decimal value of that is 118505380540.
# After modulo 109 + 7, the result is 505379714.

 

# Constraints:
#     1 <= n <= 10^5

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 0:
            return 0

        marker = 1
        bitsize = 0
        result = 0
        ceil = int(1e9+7) # 10 to the power + 7
        for i in range(1, n+1):
            while i >= marker:
                marker <<= 1
                bitsize += 1
            
            result <<= bitsize
            result |= i
            result = result % ceil
        return result




def checkAnswer(s:Solution, n: int, ans:int):
    output = s.concatenatedBinary(n)
    if output != ans:
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    checkAnswer(s, 1, 1)
    checkAnswer(s, 3, 27)
    checkAnswer(s, 12, 505379714)


