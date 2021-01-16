// 20210116.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        qsort(nums);
        return nums[nums.size() - k];
    }

    void qsort(vector<int>& nums)
    {
        return qsort_recursive(nums, 0, nums.size() - 1);
    }

    void qsort_recursive(vector<int>& nums, int low, int high)
    {
        
        if (low >= high) {
            return;
        }

        int pivot = nums[high];

        // partition the araray
        int l = low - 1;
        for (int j = low; high > j; ++j) {
            if (nums[j] < pivot) {
                ++l;
                // swap
                if (l == j) {
                    continue;
                }
                int t = nums[l];
                nums[l] = nums[j];
                nums[j] = t;
            }
        }

        // swap the pivot to the middle
        l++;    // pivot belows to 1 after where l stops
        if (high > l) {
            nums[high] = nums[l];
            nums[l] = pivot;
        }

        // after it's done, l will be the middle point
        qsort_recursive(nums, low, l - 1);
        qsort_recursive(nums, l + 1, high);
    }
};

void checkAnswer(vector<int> nums, int k, int expected)
{
    Solution s;

    _ASSERT(s.findKthLargest(nums, k) == expected);
}

int main()
{
    checkAnswer({ 3, 1, 2, 4 }, 2, 3);
    checkAnswer({ 2, 1 }, 1, 2);
    checkAnswer({ 99, 99 }, 1, 99);
    checkAnswer({ 3,2,1,5,6,4 }, 2, 5);
    checkAnswer({ 3,2,3,1,2,4,5,5,6 }, 4, 4);
}
