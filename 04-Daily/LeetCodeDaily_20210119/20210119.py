class Solution:
    def longestPalindrome(self, s:str) ->str:
        longest = 1
        long_s = 0
        slen = len(s)

        for i in range(slen):
            # check even length palindrome
            start = i
            end = i + 1
            count = -1
            while 0 <= start and slen > end and s[start] == s[end]:
                # we keep going left and right
                start -= 1
                end += 1
                count += 1
            length = end - start - 1
            if length > longest:
                longest = length
                long_s = start + 1

            # check odd length palindrome
            start = i - 1
            end = i + 1
            count = 0
            while 0 <= start and slen > end and s[start] == s[end]:
                start -= 1
                end += 1
                count += 1
            length = end - start - 1
            if length > longest:
                longest = length
                long_s = start + 1

        return s[long_s:(long_s+longest)]


if __name__ == "__main__":
    s = Solution()
    assert(s.longestPalindrome("babad") == "bab")
    assert(s.longestPalindrome("cbbd") == "bb")
    assert(s.longestPalindrome("a") == "a")
    assert(s.longestPalindrome("ac") == "a")