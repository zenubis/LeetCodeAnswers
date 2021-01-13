/* https://leetcode.com/problems/two-sum/ */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result(2);
        const int count = nums.size();
        for (int i = 0; count - 1 > i; ++i) {
            for (int j = i+1; count > j; ++j ) {
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        
        return result;
    }
};