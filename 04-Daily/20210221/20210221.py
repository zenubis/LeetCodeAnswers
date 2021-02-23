#https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3650/
# Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

#     Integers in each row are sorted in ascending from left to right.
#     Integers in each column are sorted in ascending from top to bottom.

# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true

# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     1 <= n, m <= 300
#     -10^9 <= matix[i][j] <= 10^9
#     All the integers in each row are sorted in ascending order.
#     All the integers in each column are sorted in ascending order.
#     -10^9 <= target <= 10^9

import time

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0:
            return False
        
        if n == 0:
            return False
        
        for i in range(m):
            if matrix[i][0] > target:
                return False
            elif matrix[i][0] == target or self.quickFind(matrix[i], n, target):
                return True
        return False
            
    def quickFind(self, array:list[int], length:int, target) -> bool:
        l = 0
        r = length - 1
        
        while (l < r):
            mid = (l + r) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                l = mid + 1
            elif array[mid] > target:
                r = mid - 1
        return array[l] == target

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        curr = matrix[m-1][0]
        
        i = len(matrix)-1
        j = 0
        
        while curr != target:
            if i<0 or i >= m or j<0 or j>=n: return False
            curr = matrix[i][j]
            if target < curr:
                i-=1
            elif target > curr:
                j+=1
            else:
                return True
            
        
        return curr==target

def checkAnswer(s:Solution, matrix: list[list[int]], target: int, ans):
    output = s.searchMatrix(matrix, target)
    if output != ans:
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    start = time.perf_counter()
    checkAnswer(s, [[-5]], -5, True)
        
    end = time.perf_counter()

    print(f"lapsed: {end - start}")