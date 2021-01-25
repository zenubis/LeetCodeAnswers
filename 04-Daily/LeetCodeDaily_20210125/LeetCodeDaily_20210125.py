class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        count = k   # so that if array starts with 1, we dont immediately fail it
        for n in nums:
            if n == 0:
                count += 1 
            elif count < k:
                return False
            else:
                count = 0
                continue
                
        return True
            



def checkAnswer(s:Solution, nums: list[int], k: int, ans:bool):
    output = s.kLengthApart(nums, k)
    if output != ans:
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)



s = Solution()
checkAnswer(s, [1,0,0,0,1,0,0,1], 2, True)