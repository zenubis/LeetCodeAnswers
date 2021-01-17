// LeetCodeDaily_20210117.cpp : This file contains the 'main' function. Program execution begins and ends there.
// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3607/
//
/*
Given an integer n, return the number of strings of length n that consist only of vowels 
(a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes
before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045



Constraints:
    1 <= n <= 50


*/

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
class Solution {
public:
    unordered_map<int, int> cache;
    int countVowelStrings(int n) {
        return count(n, 5);
    }

    // n is level
    // c is number to stand for vowels
    //   a = 5, e = 4, i = 3, o = 2 and u = 1
    int count(int n, int c)
    {
        if (n == 1|| c == 1) {
            return c;
        }

        // find in cache
        int key = (n << 24 | ((c-2) & 0xF));
        auto itr = cache.find(key);
        if (itr != cache.end()) {
            return itr->second;
        }

        int total = 0;
        --n;
        while (c > 0) {
            total += count(n, c--);
        }

        cache.insert(std::pair<int, int>(key, total));
        return total;
    }
};

int main()
{
    Solution s;
    _ASSERT(s.countVowelStrings(1) == 5);
    _ASSERT(s.countVowelStrings(2) == 15);
    _ASSERT(s.countVowelStrings(3) == 35);
    _ASSERT(s.countVowelStrings(4) == 70);
    _ASSERT(s.countVowelStrings(33) == 66045);
}
