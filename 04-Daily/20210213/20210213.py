# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3638/
# In an N by N square grid, each cell is either empty (0) or blocked (1).

# A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

#     Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
#     C_1 is at location (0, 0) (ie. has value grid[0][0])
#     C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
#     If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

# Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

# Example 1:
# Input: [[0,1],[1,0]]
# Output: 2

# Example 2:
# Input: [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4


# Note:

#     1 <= grid.length == grid[0].length <= 100
#     grid[r][c] is 0 or 1

import collections
import math

# using A* path finding
class Node:
    # G is the distance between the current node and the start node.
    # H is the heuristic — estimated distance from the current node to the end node.
    # F is the total cost of the node. ie, g + h
    def __init__(self, x:int, y:int, g:int, dest_x:int, dest_y:int):
        self.x = x
        self.y = y
        self.g = g
        dx = dest_x - x
        dy = dest_y - y
        if dx < dy:
            self.f = self.g + dx + (dy - dx)
        else:
            self.f = self.g + dy + (dx - dy)
    
    def __lt__(self, rhs):
        return rhs and self.f < rhs.f

    def __str__(self):
        return f"[[{self.x}, {self.y}], {self.g}, {self.f}]"


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        grid_size = len(grid)
        open_list = [Node(0, 0, 1, grid_size, grid_size)]
        close_list = set()

        while open_list:
            candidate = collections._heapq.heappop(open_list)
            close_list.add((candidate.x, candidate.y))
            if candidate.x == grid_size - 1 and candidate.y == grid_size - 1:
                return candidate.g
            
            #add all neighbours of candidate
            self.addNeighbour(open_list, close_list, candidate, grid, grid_size)

        return -1

    def addNeighbour(self, open_list:list, close_list:set, candidate:Node, grid:list[list[int]], grid_size:int):
        for ix in range(-1, 2):
            for iy in range(-1, 2):
                if ix == 0 and iy == 0:
                    continue

                new_x = candidate.x + ix
                new_y = candidate.y + iy
                
                #check bounds
                if new_x < 0 or new_x >= grid_size or new_y < 0 or new_y >= grid_size or grid[new_x][new_y] == 1:
                    continue

                new_node = Node(new_x, new_y, candidate.g + 1, grid_size, grid_size)
            
                # is it already explored
                if (new_node.x, new_node.y) in close_list:
                    continue

                # if node in open_list
                found = False
                for x in open_list:
                    if x.x == new_node.x and x.y == new_node.y:
                        found = True

                        # and g value is smaller            
                        if x.g > new_node.g:
                            x.g = new_node.g
                            x.f = new_node.f
                            collections._heapq.heapify(open_list)
                            break
                if found:
                    continue
                collections._heapq.heappush(open_list, new_node)
             



def checkAnswer(s:Solution, grid: list[list[int]], ans):
    output = s.shortestPathBinaryMatrix(grid)
    if output != ans:
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    
    checkAnswer(s, [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]], 10)
    checkAnswer(s, [[0,0,1,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0],[0,1,1,0,1,1,1,1,1],[0,0,0,1,0,0,0,0,0],[1,1,0,0,0,1,0,0,0],[1,0,1,0,0,1,0,0,1],[1,1,1,1,0,0,1,0,0],[1,0,0,1,0,0,1,1,1],[0,0,0,0,0,0,0,0,0]], 11)
    checkAnswer(s, [[0,1],[1,0]], 2)
    checkAnswer(s, [[0,0,0],[1,1,0],[1,1,0]], 4)

#   0 1 2 3 4 5 6 7 8    
#0 [0,0,1,0,0,1,0,1,0]
#1 [0,0,0,0,0,0,0,0,0]
#2 [0,1,1,0,1,1,1,1,1]
#3 [0,0,0,1,0,0,0,0,0]
#4 [1,1,0,0,0,1,0,0,0]
#5 [1,0,1,0,0,1,0,0,1]
#6 [1,1,1,1,0,0,1,0,0]
#7 [1,0,0,1,0,0,1,1,1]
#8 [0,0,0,0,0,0,0,0,0]
    
#   0 1 2 3 4 5 6
#0 [0,0,1,0,0,0,0]
#1 [0,1,0,0,0,0,1]
#2 [0,0,1,0,1,0,0]
#3 [0,0,0,1,1,1,0]
#4 [1,0,0,1,1,0,0]
#5 [1,1,1,1,1,0,1]
#6 [0,0,1,0,0,0,0]