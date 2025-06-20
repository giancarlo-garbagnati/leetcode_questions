"""
680. Valid Palindrome II
Solved
Easy

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""

import math
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            # original palindrome solution, might actually be faster
            #for i in range(math.floor(len(s)/2)):
            #    if s[i] != s[len(s)-1-i]:
            #        return False
            #return True
            return s == s[::-1]

        if is_palindrome(s):
            return True

        s_list = list(s)

        # original solution, only passed ~400 test cases
        #for i in range(len(s_list)):
        #    st = s_list[:i] + s_list[i+1:]
        #    if is_palindrome(''.join(st)):
        #        return True 
        #return False

        for i in range(math.floor(len(s_list)/2)):
            if s_list[0] != s_list[-1]:
                return is_palindrome(s_list[1:]) or is_palindrome(s_list[:-1])
            else:
                s_list = s_list[1:-1]
