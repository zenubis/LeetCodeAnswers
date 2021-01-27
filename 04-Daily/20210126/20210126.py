# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3617/

# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
#  where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), 
# and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, 
# down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# Example 2:
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:
# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

# Constraints:
#     rows == heights.length
#     columns == heights[i].length
#     1 <= rows, columns <= 100
#     1 <= heights[i][j] <= 106

import heapq

class Node:
    height = 0
    x = 0
    y = 0

    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y
    
    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y and self.height == rhs.height

    def __lt__(self, rhs):
        return self.height < rhs.height

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        explored = []
        
        # since we always starts at (0, 0), we can always start the list with (0, 1) and (1, 0) 
        candidates = [Node(heights[0][1], 0, 1), Node(heights[1][0], 1, 0)]
        heapq.heapify(candidates)

        lowest = 0  #lowest path

    



   

def checkAnswer(s:Solution, heights: list[list[int]], ans:int):
    output = s.minimumEffortPath(heights)
    if output != ans:
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    checkAnswer(s, [[1,2,2],[3,8,2],[5,3,5]], 2)
    checkAnswer(s, [[1,2,3],[3,8,4],[5,3,5]], 1)
    checkAnswer(s, [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]], 0)

