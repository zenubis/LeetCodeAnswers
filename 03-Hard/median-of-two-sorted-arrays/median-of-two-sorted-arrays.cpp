/* https://leetcode.com/problems/median-of-two-sorted-arrays/ */

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int median = (nums1.size() + nums2.size());
        bool isOdd = (median & 0x1) == 0;   // array total is even, need to add with next number to get median
        median >>= 1; // divide by 2

        int p1 = 0;
        int p2 = 0;
        int med1, med2;
        med1 = med2 = 0;
        while (p1 + p2 <= median) {
            if (IsNum1Smaller(nums1, p1, nums2, p2)) {
                med2 = med1;
                med1 = nums1[p1++];
            }
            else {
                med2 = med1;
                med1 = nums2[p2++];
            }
        }

        if (isOdd) {
            return ((double)med2 + (double)med1) / 2.0;
        }

        return med1;
    }

    static bool IsNum1Smaller(vector<int>& nums1, int p1, vector<int>& nums2, int p2)
    {
        if (p1 < nums1.size()) {
            if (p2 < nums2.size() && nums1[p1] > nums2[p2]) {
                return false;
            }
            else {
                // num2 exhausted
                return true;
            }
        }
        
        // num1 exhausted
        return false;
    }
};