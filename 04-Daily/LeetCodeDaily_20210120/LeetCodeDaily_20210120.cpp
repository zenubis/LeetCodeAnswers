// LeetCodeDaily_20210120.cpp : This file contains the 'main' function. Program execution begins and ends there.
// https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3610/
/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true



Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.


*/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        std::vector<char> stack;
        for (char c : s) {
            switch (c) {
                case '(':
                case '{':
                case '[':
                    stack.push_back(c);
                    break;
                case ')':
                    if (!PopAndCheck(stack, '(')) {
                        return false;
                    }
                    break;
                case '}':
                    if (!PopAndCheck(stack, '{')) {
                        return false;
                    }
                    break;
                case ']':
                    if (!PopAndCheck(stack, '[')) {
                        return false;
                    }
                    break;
                default:
                    return false;
            }
        }

        return stack.empty();
    }

    bool PopAndCheck(vector<char>& stack, char c)
    {
        if (stack.empty()) {
            return false;
        }

        char check = stack.back();
        stack.pop_back();
        return c == check;
    }
};

int main()
{
    std::cout << "Hello World!\n";
}
