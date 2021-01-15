// 20210115.cpp
//

// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3605/
/*
You are given an integer n. An array nums of length n + 1 is generated in the following way:

    nums[0] = 0
    nums[1] = 1
    nums[2 * i] = nums[i] when 2 <= 2 * i <= n
    nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n

Return the maximum integer in the array nums​​​.


Example 1:
Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.

Example 2:
Input: n = 2
Output: 1
Explanation: According to the given rules, the maximum between nums[0], nums[1], and nums[2] is 1.

Example 3:
Input: n = 3
Output: 2
Explanation: According to the given rules, the maximum between nums[0], nums[1], nums[2], and nums[3] is 2.


Constraints:
    0 <= n <= 100

*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int getMaximumGenerated(int n) {
        // brute force, generate the array
        vector<int> nums;

        if (n == 0) {
            return 0;
        }

        nums.push_back(0);
        nums.push_back(1);

        int largest = 1;
        for (int i = 1; n >= (2 * i); ++i) {

            nums.push_back(nums[i]);
            if (n >= 2 * i + 1) {
                int result = nums[i] + nums[i + 1];
                largest = std::max(largest, result);
                nums.push_back(result);
            }
        }

        return largest;
    }


    void printArray(vector<int>& array) {

        printf("------------------ [%d]\n", array.size());
        if (array.empty()) {
            return;
        }

        const int STEPPING = 30;

        for (int i = 0; array.size() > i; i+= STEPPING) {
            printf("-");
            for (int j = 0; STEPPING > j; ++j) {
                printf("%4d ", i+j);
            }
            printf("\n");
            printf(" ");
            for (int j = 0; STEPPING > j && array.size() > j + i; ++j) {
                printf("%4d ", array[i+j]);
            }

            printf("\n");
        }
        
    }
};

int main()
{
    Solution s;

    _ASSERT(s.getMaximumGenerated(20) == 7);
    _ASSERT(s.getMaximumGenerated(2) == 1);
    _ASSERT(s.getMaximumGenerated(3) == 2);
}