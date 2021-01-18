// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3603/
/*
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

 

Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 104
    1 <= x <= 109


*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minOperations(vector<int> nums, int x) {
        int target = 0;
        for (int y : nums) {
            target += y;
        }
        
        if (target == x) {
            return nums.size();
        }

        target -= x;

        int largest = 0;
        int start = 0;
        int end = 0;
        int total = 0;
        for (int i = 0; nums.size() > i; ++i) {
            end = i;
            total += nums[end];
            while (target < total && start < end) {
                total -= nums[start++];
            }

            if (total == target) {
                largest = std::max(largest, (end - start) + 1);                
            }
        }

        if (largest == 0) {
            return -1;
        }

        return nums.size() - largest;
    }
};

int main()
{
    Solution s;

    _ASSERT(16 == s.minOperations({ 8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309 }, 134365));
    _ASSERT(-1 == s.minOperations({ 1, 1 }, 3));
    _ASSERT(1  == s.minOperations({ 5, 2, 3, 1, 1 }, 5));
    _ASSERT(2  == s.minOperations({ 1, 1, 4, 2, 3 }, 5));
    _ASSERT(-1 == s.minOperations({ 5,6,7,8,9 }, 4));
    _ASSERT(5  == s.minOperations({ 3,2,20,1,1,3 }, 10));
}