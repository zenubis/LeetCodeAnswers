#https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631/

# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

# Example 1:
# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]

# Example 2:
# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]
 
# Constraints:
#     1 <= s.length <= 10^4
#     s[i] and c are lowercase English letters.
#     c occurs at least once in s.



class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        l = len(s)
        prev = -1
        result = [0] * l
        for i in range(l):
            if s[i] == c[0]:
                # update all the values from prev to here
                self.writeIndex(result, prev, i)
                prev = i

        if prev < l:
            for i in range(prev+1, l):
                result[i] = i-prev

        return result
                
    def writeIndex(self, list, start, end):
        if start < 0:
            for i in range(0, end):
                list[i] = end - i
            return

        start = start + 1 #start does not need to update, so we ++
        mid = (start + end) // 2
        
        for i in range(start, mid):
                list[i] = i - start + 1
        for i in range(mid, end):
                list[i] = end - i

        


def checkList(lhs, rhs):
    l = len(lhs)
    if l != len(rhs):
        return False
    for i in range(l):
        if lhs[i] != rhs[i]:
            return False
    return True

def checkAnswer(s:Solution, st: str, c: str, ans):
    output = s.shortestToChar(st, c)
    if not checkList(ans, output):
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    checkAnswer(s, "abaa", "b", [1,0,1,2])
    checkAnswer(s, "loveleetcode", "e", [3,2,1,0,1,0,0,1,2,2,1,0])
    checkAnswer(s, "aaab", "b", [3,2,1,0])
    checkAnswer(s, "aaba", "b", [2,1,0,1])
    