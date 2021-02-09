# https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3629/
# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

# In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

# The canonical path should have the following format:

#     The path starts with a single slash '/'.
#     Any two directories are separated by a single slash '/'.
#     The path does not end with a trailing '/'.
#     The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

# Return the simplified canonical path.

 

# Example 1:

# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.

# Example 2:

# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

# Example 3:

# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

# Example 4:

# Input: path = "/a/./b/../../c/"
# Output: "/c"

 
# Constraints:
#     1 <= path.length <= 3000
#     path consists of English letters, digits, period '.', slash '/' or '_'.
#     path is a valid absolute Unix path.
import collections


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = collections.deque()
        

        for x in path_list:
            if x == None or x == "." or x == "":
                continue
            elif x == "..":
                try:
                    stack.pop()
                except IndexError:
                    pass
                
            else:
                stack.append(x)

        return "/" + "/".join(stack)



def CheckAnswer(s:Solution, input, ans):
    output = s.simplifyPath(input)
    if output != ans:
        print(output)
        assert(False)

if __name__ == "__main__":
    s = Solution()
    CheckAnswer(s, "/a/../../b/../c//.//", "/c")
    CheckAnswer(s, "/home/", "/home")
    CheckAnswer(s, "/../", "/")
    CheckAnswer(s, "/home//foo/", "/home/foo")
    CheckAnswer(s, "/a/./b/../../c/", "/c")
    
    