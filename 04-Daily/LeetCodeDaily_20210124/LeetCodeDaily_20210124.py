# https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3615/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        ret = "{0}".format(self.val)
        cur = self.next
        while cur:
            ret += "->{0}".format(cur.val)
            cur = cur.next
        return ret

    @staticmethod
    def MakeListStr(string:str):
        root = ListNode(0)
        current = root
        l = string.split("->")
        for n in l:
            newnode = ListNode(int(n))
            current.next = newnode
            current = newnode
        root = root.next
        return root

    @staticmethod
    def MakeList(nums:list):
        root = ListNode(0)
        current = root
        for n in nums:
            newnode = ListNode(n)
            current.next = newnode
            current = newnode
        root = root.next
        return root
        
    def equal(self, rhs):
        if not isinstance(rhs, ListNode):
            return False

        if not self.val == rhs.val:
            return False
        
        cur = self.next
        cur2 = rhs.next
        while cur != None and cur2 != None:
            if cur.val != cur2.val:
                return False
            cur = cur.next
            cur2 = cur2.next
            
        return cur == None and cur2 == None


import heapq

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        ret = ListNode(0)
        numlist = len(lists)
        heap = []

        for i in range(numlist):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        if not heap:
            return None

        cur = ret
        while heap:
            (num, index) = heapq.heappop(heap)
            
            cur.next = lists[index]
            cur = cur.next
            
            if lists[index].next != None:
                lists[index] = lists[index].next
                heapq.heappush(heap, (lists[index].val, index))
                

        ret = ret.next
        
        return ret            

            


        

def checkAnswer(s:Solution, lists: list[ListNode], ans:ListNode):
    output = s.mergeKLists(lists)
    if output == None and ans == None:
        return

    if not output.equal(ans):
        print("Wrong answer")
        print("output:", output)
        print("answer:", ans)
        assert(False)


s = Solution()
checkAnswer(s, [ListNode.MakeList([1,4,5]), ListNode.MakeList([1,3,4]),ListNode.MakeList([2,6])], ListNode.MakeListStr("1->1->2->3->4->4->5->6" ))
checkAnswer(s, [], None)
checkAnswer(s, [[]], None)

