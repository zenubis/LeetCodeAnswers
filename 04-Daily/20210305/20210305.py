# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        
        if None == root:
            return [0]
        
        ans = [root.val]
        count = [1]
        
        size = 1
        
        if root.left:
            size = self.compute(root.left, 1, size, ans, count)
        if root.right:
            size = self.compute(root.right, 1, size, ans, count)
        
        for x in range(1, size):
            ans[x] = ans[x] / count[x]
            
        return ans
        
        
    def compute(self, node, level:int, size:int, ans: list[float], count:list[int]):
        while level >= size:
            ans.append(0)
            count.append(0)
            size += 1
            
        ans[level] += node.val
        count[level] += 1
        level += 1
        
        if node.left:
            size = self.compute(node.left, level, size, ans, count)
        if node.right:
            size = self.compute(node.right, level, size, ans, count)
        
        return size
        
        
def MakeListInternal(parent:TreeNode, index:int, nums:list[int], count:int):
    childindex = index * 2 + 1
    if childindex < count:
        parent.left = TreeNode(nums[childindex])
        MakeListInternal(parent.left, childindex, nums, count)
    
    childindex += 1
    if childindex < count:
        parent.right = TreeNode(nums[childindex])
        MakeListInternal(parent.right, childindex, nums, count)

def MakeList(nums:list[int]):
    count = len(nums)

    root = TreeNode(nums[0])
    MakeListInternal(root, 0, nums, count)
    return root


def checkList(lhs, rhs):
    l = len(lhs)
    if l != len(rhs):
        return False
    for i in range(l):
        if lhs[i] != rhs[i]:
            return False
    return True

def checkAnswer(s:Solution, root:TreeNode, ans):
    output = s.averageOfLevels(root)
    if not checkList(ans, output):
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    checkAnswer(s, MakeList([3,9,20,15,7]), [3, 14.5, 11])
    