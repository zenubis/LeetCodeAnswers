// LeetCodeDaily_20210119.cpp : This file contains the 'main' function. Program execution begins and ends there.
// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3609/

#include <iostream>
#include <string>


using namespace std;

class Solution {
public:
    string longestPalindrome(string& s) {
        const int len = s.size();
        int longest = 1;    // the length of our longest palindrome. 
                            // start at 1 because first single char can be 
                            // considered a palindrome
        int long_s = 0;     // the index the palindrom starts at
        int count;         // temp worker variable

        int start = 0;      // worker variable, start index of the substring we testing
        int end = 0;        // worker variable, end index of the substring we testing
        int length = 0;     // worker variable, to store length of substring
        for (int i = 0; len - 1 > i; ++i) {
            // check even length palindrome
            start = i;
            end = i + 1;
            count = -1;
            while (start >= 0 && end < len && s[start] == s[end]) {
                // try to keep expanding until we're no longer a palindrome
                --start;
                ++end;
                ++count;
            }
            // simplified form of "length = end - start + 1 - 2 
            // (-2 because start and end are both 1 more than they actually are)
            length = end - start - 1;   // if not palindrome, length will be 0
            if (length > longest) {
                longest = length;
                long_s = i - count;
            }
            
            // check odd length palindrome
            start = i - 1;
            end = i + 1;
            count = 0;
            while (start >= 0 && end < len && s[start] == s[end]) {
                --start;
                ++end;
                ++count;
            }
            length = end - start - 1;   // length at least 1 because, index "i" itself is a palindrome
            if (length > longest) {
                longest = length;
                long_s = i - count;
            }
        }

        return s.substr(long_s, longest);
    }

};

int checkString(Solution& s, string str, string ans)
{
    return s.longestPalindrome(str).compare(ans);
}

int main()
{
    Solution s;
    _ASSERT(0 == checkString(s, "ccc", "ccc"));
    _ASSERT(0 == checkString(s, "babad", "bab"));
    _ASSERT(0 == checkString(s, "cbbd", "bb"));
    _ASSERT(0 == checkString(s, "a", "a"));
    _ASSERT(0 == checkString(s, "ac", "a"));
}
