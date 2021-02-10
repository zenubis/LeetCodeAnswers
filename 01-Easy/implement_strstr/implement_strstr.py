# https://leetcode.com/problems/implement-strstr/

# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0

# Constraints:

#     0 <= haystack.length, needle.length <= 5 * 10^4
#     haystack and needle consist of only lower-case English characters.


class Solution:
    # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
    # Boyer Moore Search string method
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        
        if len_needle == 0:
            return 0

        len_hay = len(haystack)
        i = 0
        while i <= (len_hay - len_needle) :
            j = len_needle - 1
            while j >= 0:
                if haystack[i + j] != needle[j]:
                    #search haystack[i+j] if it exists in needle anywhere
                    k = j - 1
                    while k >= 0:
                        if haystack[i + j] == needle[k]:
                            i = i + j - k - 1
                            break
                        k -= 1
                    if k < 0:
                        i = i + j
                    break
                j -= 1

            if j < 0:
                return i
            i += 1

        return -1

    # brute force method
    # def strStr(self, haystack: str, needle: str) -> int:
    #     len_needle = len(needle)
        
    #     if len_needle == 0:
    #         return 0
        
    #     len_hay = len(haystack)
        
        
    #     for i in range(len_hay - len_needle + 1):
    #         # we have a chance, try to find the rest of the string
    #         if haystack[i] == needle[0]:
    #             found = True
    #             for j in range(1, len_needle):
    #                 if haystack[i+j] != needle[j]:
    #                     found = False
    #                     break
                
    #             if found:
    #                 return i
                
        
    #     return -1

def checkAnswer(s:Solution, haystack: str, needle: str, ans):
    output = s.strStr(haystack, needle)
    if ans != output: 
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    checkAnswer(s, "ababbbbaaabbbaaa", "bbbb", 3)

    checkAnswer(s, "mississippi", "issip", 4)
    checkAnswer(s, "hello", "ll", 2)
    checkAnswer(s, "aaaaa", "bba", -1)
    checkAnswer(s, "", "", 0)
    