// LeetCode2021JanWeek2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/580/week-2-january-8th-january-14th/3603/

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