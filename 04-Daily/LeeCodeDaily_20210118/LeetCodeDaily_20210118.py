
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        lookup = {}
        pair = 0
        for x in nums:
            search = k - x
            if search in lookup and lookup[search] > 0:
                lookup[search] -= 1
                pair += 1
                continue

            if x in lookup:
                lookup[x] += 1
            else:
                lookup[x] = 1
        return pair


s = Solution()

print(s.maxOperations([1, 2, 3, 4], 5))

