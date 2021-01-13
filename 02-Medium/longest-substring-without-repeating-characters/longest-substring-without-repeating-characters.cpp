/* https://leetcode.com/problems/longest-substring-without-repeating-characters/ */
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        char lookup[128];
        int longest = 0;
        int current = 0;
        char c;
        int count = s.size();
        for(int i = 0; count > i; ++i) {
            c = s[i];
            memset(lookup, 0, sizeof(char) * 128);
            lookup[c] = 1;
            current = 1;
            
            for (int j = i + 1; count > j; ++j) {
                c = s[j];
                if (lookup[c] != 0) {
                    break;
                }
                lookup[c] = 1;
                current++;
            }
            
            if (longest < current) {
                longest = current;
            }
        }
        
        if (longest < current) {
            return current;
        }
        
        return longest;
    }
};