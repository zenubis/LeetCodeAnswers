import heapq

class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            smallest = nums[0]
            for x in range(1, len(nums)):
                if smallest > nums[x]:
                    smallest = nums[x]
            return [smallest]

        slen = len(nums)
        result = nums[:-k+1]
        heap = []
        for x in range(len(result)):
            heap.append((result[x], x))
        
        result = []
        heapq.heapify(heap)
        min_index = -1
        while k > 0:
            (n, index) = heapq.heappop(heap)
            if index > min_index:
                min_index = index
                result.append(n)
                k-=1
                
                if slen - min_index - 1 <= k:
                    if k > 0:
                        return result + nums[-k:]
                    else:
                        return result
                
                if k > 0:
                    heapq.heappush(heap, (nums[slen-k], slen-k))

        return result


    def mostCompetitive_brute(self, nums: list[int], k: int) -> list[int]:
        slen = len(nums)
        if k == slen:
            return nums

        start = 0
        end = slen - 1
        result = []
        
        while (0 < k):
            smallest = self.findSmallest(nums, start, end, k)
            smallest2 = smallest
            while (smallest2+1 < slen and nums[smallest2+1] == nums[smallest]):
                smallest2 += 1
            if (smallest == smallest2):
                result.append(nums[smallest])
            else:
                #we have this much, but do we need that much?
                if (smallest2 - smallest + 1 > k):
                    result = result + nums[smallest:smallest+k]
                else:
                    result = result + nums[smallest:smallest2+1]
                
            k -= smallest2 - smallest + 1
            start = smallest2 + 1
            if end - start + 1 <= k:
                return result + nums[start:]

        return result
        

    def findSmallest(self, nums:list[int], s:int, e:int, k:int) -> int:
        smallest = s
        for i in range(s+1, e - k + 2):
            if nums[smallest] > nums[i]:
                smallest = i
        
        return smallest

def CheckAnswer(s:Solution, nums:list[int], k:int, ans:list[int]):
    out = s.mostCompetitive(nums, k)
    if (out != ans):
        print('wrong answer')
        print(ans)
        print(out)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    CheckAnswer(s, [74,80,88,14,97,53,51,29,83,91,18,9,56,86,74,86,21,18,91,70,100,25,67,16,37,35,92,74,40,58,2,94,47,55,36,18,41,31,32,59,77,64,41,37,59,16,0,25,88,35,76,17,70,73,35,15,46,72,66,44,83,74,61,63,78,14,70,96,65,47,64,35,29,19,6,95,21,49,40,52,70,91,61,21,16,73,83,35,30,33,49,2,59,8,6,7,37,91,51,43,53,67,90,25,55,46,56,79,99,70,69,48,83,23,84,36,52,36,93,40,60,99,83], 1, [0])
    CheckAnswer(s, [65,35,89,39,25,0,42,87,15], 3, [0,42,15])
    CheckAnswer(s, [3,5,2,6], 2, [2,6])
    CheckAnswer(s, [2,4,3,3,5,4,9,6], 4, [2,3,3,4])
    CheckAnswer(s, [71,18,52,29,55,73,24,42,66,8,80,2], 3, [8,80,2])
    CheckAnswer(s, [84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71], 24, [10,23,61,62,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71])
    CheckAnswer(s, [2,10,3,5,9,4,2,0,6,7,8,0,6,5,8,1,6,1,5,5,2,10,9,5,7,7,3,2,1,4,0,7,0,3,10,10,5,10,4,7,0,2,10,9,0,2,6,10,6,9,2,1,9,8,7,2,0,7,3,6,2,1,8,0,0,0,10,4,3,5,0,8,1,8,5,1,6,0,4,4,10,2,0,5,1,1,3,3,5,2,6,5,6,0,3,8,0,1,7,0,0,9,6,10,5,9,8,9,8,7,8,10,6,3,8,0,5,7,4,3,5,7,7,0,3,10,1,3,10,2,10,3,2,6,3,10,8,10,6,0,7,6,2,10,4,0,7,4,8,8,1,7,1,4,9,7,7,8,9,8,7,2,4,9,8,8,0,8,2,10,7,3,10,8,5,1,1,3,0,5,1,7,1,7,9,2,6,9,6,10,6,1,7,8,3,6,9,3,5,9,0,9,3,5,8,4,6,8,10,8,0,9,3,7,10,4,4,2,3,7,2,10,3,5,4,9,9,2,1,2,10,4,4,4,3,5,9,7,2,0,3,6,6,7,3,9,4,6,9,7,1,3,2,3,6,6,1,7,10,0,4,10,3,5,0,10,3,10,3,0,0,1,6,6,5,9,10,5,5,9,0,5,4,1,10,2,3,1,7,9,10,10,4,3,5,9,5,4,4,8,0,1,8,1,4,6,5,6,0,6,8,6,5,6,5,7,9,5,8,8,4,2,0,0,2,9,4,9,2,6,5,2,2,8,5,4,10,8,7,7,3,4,2,0,4,3,8,6,1,7,10,10,7,4,0,6,6,0,5,6,10,3,8,3,2,4,10,4,3,0,4,10,7,6,0,4,7,0,5,2,5,2,10,9,1,10,9,6,6,5,9,10,1,3,5,2,0,6,8,5,6,3,4,8,4,0,7,0,7,9,9,1,4,6,4,5,7,3,0,4,4,9,10,5,10,3,9,6,6,2,9,4,0,4,3,3,1,7,2,1,0,2,6,7,1,1,0,3,9,8,9,4,6,3,10,7,3,1,5,2,0,3,9,5,3,3,3,1,7,5,8,10,10,8,0,2,3,3,2,9,3,1,3,9,0,1,8,2,1,6,0,6,3,1,3,1,10,5,6,0,4,7,10], 79, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,3,3,2,9,3,1,3,9,0,1,8,2,1,6,0,6,3,1,3,1,10,5,6,0,4,7,10])

    
    

