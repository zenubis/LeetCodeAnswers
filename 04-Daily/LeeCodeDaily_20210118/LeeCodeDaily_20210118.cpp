// LeeCodeDaily_20210118.cpp : This file contains the 'main' function. Program execution begins and ends there.
// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3608/
/*
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.



Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.



Constraints:

    1 <= nums.length <= 105
    1 <= nums[i] <= 109
    1 <= k <= 109


*/

#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> lookup;
        
        int search = 0;
        int pair_found = 0;
        for (auto n : nums) {
            search = k - n;
            auto itr = lookup.find(search);
            if (itr != lookup.end() && 0 < itr->second) {
                pair_found++;
                itr->second--;
                continue;
            }
            
            itr = lookup.find(n);
            if (itr != lookup.end()) {
                itr->second++;
            }
            else {
                lookup.insert(unordered_map<int, int>::value_type(n, 1));
            }
        }

        return pair_found;
    }
};

void CheckAnswer(Solution& s, vector<int> nums, int k, int answer)
{
    _ASSERT(s.maxOperations(nums, k) == answer);
}

int main()
{
    Solution s;
    CheckAnswer(s, {1, 2, 3, 4}, 5, 2);
    CheckAnswer(s, {3, 1, 3, 4, 3}, 6, 1);
}
