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
import time
from collections import _heapq

# using A* path finding
class Node:
    # G is the distance between the current node and the start node.
    # H is the heuristic — estimated distance from the current node to the end node.
    # F is the total cost of the node. ie, g + h
    def __init__(self, x:int, y:int, g:int, grid_size:int, parent = None):
        self.x = x
        self.y = y
        self.g = g
        self.parent = parent
        dx = grid_size - x
        dy = grid_size - y
        if dx < dy:
            self.f = self.g + dx + (dy - dx)
        else:
            self.f = self.g + dy + (dx - dy)

    def copy(self, other):
        self.x = other.x
        self.y = other.y
        self.g = other.g
        self.f = other.f
        self.parent = other.parent

    def printPath(self):
        if self.parent:
            self.parent.printPath()
        print(self)
    
    def __lt__(self, rhs):
        return rhs and self.f < rhs.f

    def __str__(self):
        return f"[[{self.x}, {self.y}], {self.g}, {self.f}]"


class Solution:
    direction = [
        (-1, -1), ( 0, -1), ( 1, -1),
        (-1,  0),           ( 1,  0),
        (-1,  1), ( 0,  1), ( 1,  1),
    ]

    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        grid_size = len(grid)
        start = Node(0, 0, 1, grid_size)
        open_list = [start]
        lookup = { (start.x, start.y) : start }
        close_list = set()

        while open_list:
            candidate = _heapq.heappop(open_list)
            del lookup[(candidate.x, candidate.y)]
            close_list.add((candidate.x, candidate.y))

            # check if we're at goal
            if candidate.x == grid_size - 1 and candidate.y == grid_size - 1:
                # print("the winning path:")
                # candidate.printPath()
                return candidate.g
            
            #add all neighbours of candidate
            self.addNeighbour(open_list, close_list, lookup, candidate, grid, grid_size)

        return -1

    def addNeighbour(self, open_list:list, close_list:set, lookup:dict, candidate:Node, grid:list[list[int]], grid_size:int):
        
        for d in self.direction:
            
            new_x = candidate.x + d[0]
            new_y = candidate.y + d[1]
            
            #check bounds
            if 0 > new_x or new_x >= grid_size or 0 > new_y or new_y >= grid_size or grid[new_x][new_y] == 1:
                continue

            # is it already explored
            if (new_x, new_y) in close_list:
                continue

            new_node = Node(new_x, new_y, candidate.g + 1, grid_size, candidate)
        
            # if node is in open_list
            try:
                node = lookup[(new_x, new_y)]
                # and g value is smaller
                if node.g > new_node.g:
                    # we replace it
                    node.copy(new_node)
                    # since we changed the value, heap structure is invalid
                    # need to re-heapify it
                    _heapq.heapify(open_list)
                continue
            except KeyError:
                pass
            
            _heapq.heappush(open_list, new_node)
            lookup[(new_node.x, new_node.y)] = new_node

def printList(thelist:list):
    l = sorted(thelist, key=lambda elem:elem.f)
    for x in l:
        print(x)

def checkAnswer(s:Solution, grid: list[list[int]], ans):
    output = s.shortestPathBinaryMatrix(grid)
    if output != ans:
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    start = time.perf_counter()
    checkAnswer(s, [[0,0,1,0,0,1,0,1,0],[0,0,0,0,0,0,0,0,0],[0,1,1,0,1,1,1,1,1],[0,0,0,1,0,0,0,0,0],[1,1,0,0,0,1,0,0,0],[1,0,1,0,0,1,0,0,1],[1,1,1,1,0,0,1,0,0],[1,0,0,1,0,0,1,1,1],[0,0,0,0,0,0,0,0,0]], 11)
    checkAnswer(s, [[0,1],[1,0]], 2)
    checkAnswer(s, [[0,0,0],[1,1,0],[1,1,0]], 4)
    checkAnswer(s, [[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]], 10)
    
    checkAnswer(s, [[1,0,0],[1,1,0],[1,1,0]], -1)
    checkAnswer(s, [[0,0,0],[1,1,0],[1,1,1]], -1)
    end = time.perf_counter()

    print(f"lapsed: {end - start}")
    

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