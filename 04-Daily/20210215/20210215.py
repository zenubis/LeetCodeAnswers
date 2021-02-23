# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/
# Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
# return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

# A row i is weaker than row j, if the number of soldiers in row i is less than the number of
# soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers
# are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

# Example 1:
# Input: mat = 
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 
# k = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers for each row is: 
# row 0 -> 2 
# row 1 -> 4 
# row 2 -> 1 
# row 3 -> 2 
# row 4 -> 5 
# Rows ordered from the weakest to the strongest are [2,0,3,1,4]

# Example 2:
# Input: mat = 
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]], 
# k = 2
# Output: [0,2]
# Explanation: 
# The number of soldiers for each row is: 
# row 0 -> 1 
# row 1 -> 4 
# row 2 -> 1 
# row 3 -> 1 
# Rows ordered from the weakest to the strongest are [0,2,3,1]
# Constraints:
#     m == mat.length
#     n == mat[i].length
#     2 <= n, m <= 100
#     1 <= k <= m
#     matrix[i][j] is either 0 or 1.

import time

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        m = range(len(mat))
        ln = len(mat[0])
        n = range(ln)

        result = []
        for i in m:
            added = False
            for j in n:
                if mat[i][j] == 0:
                    added = True
                    result.append([j, i])
                    break
            if not added:
                result.append([ln, i])
        
        result = sorted(result, key=lambda elem:elem[0])
        
        r = []
        for i in range(k):
            r.append(result[i][1])

        return r



    # def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        
    #     m = len(mat)
    #     can = [True] * m
       
    #     count = 0
    #     result = []
    #     m = range(m)
    #     for i in range(len(mat[0])):
    #         for j in m:
    #             if not can[j]:
    #                 continue
                    
    #             if 0 == mat[j][i]:
    #                 result.append(j)
    #                 count += 1
    #                 if count >= k:
    #                     return result
    #                 can[j] = False
        
    #     for i in m:
    #         if can[i]:
    #             result.append(i)
    #             count += 1
    #             if count >= k:
    #                 return result
                    
    #     return []

def equal(out, ans):
    l = len(out)
    if l != len(ans):
        return False
    for i in range(l):
        if out[i] != ans[i]:
            return False
    return True

def checkAnswer(s:Solution, mat: list[list[int]], k: int, ans):
    output = s.kWeakestRows(mat, k)
    if not equal(output, ans):
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    start = time.perf_counter()
    checkAnswer(s, [
            [1,0],
            [1,0],
            [1,0],
            [1,1]
        ], 4,
        [0,1,2,3])

    checkAnswer(s, [
            [1,1,0,0,0],
            [1,1,1,1,0],
            [1,0,0,0,0],
            [1,1,0,0,0],
            [1,1,1,1,1]
        ], 3, 
        [2, 0, 3])

    checkAnswer(s, [
            [1,0,0,0],
            [1,1,1,1],
            [1,0,0,0],
            [1,0,0,0]
        ], 2,
        [0,2])
    
        
    end = time.perf_counter()

    print(f"lapsed: {end - start}")
    