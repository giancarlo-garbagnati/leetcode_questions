"""
5. Longest Palindromic Substring
Solved
Medium
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# This was a lot longer of a function than I expected, but it had a decent performance.
# Essentially, checking for 3- or 2- palindrome "bases" then expanding from that to
# check each palindrome (without having to check every length string).

class Solution(object):
    def longestPalindrome(self, s):
    
        if len(s) <= 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
    
        longest_len = 1
        longest_pal = s[0]
        
        for i, c in enumerate(list(s)):
            if i == len(s)-1: # short circuit
                break
            elif i == len(s) - int(longest_len/2): # short circuit
                break
            else:
                    
                # 3-letter palindrome base
                if (i > 0) and (s[i-1] == s[i+1]):
                    start = i-1
                    end = i+1
                    pal = s[start:end+1]
                    if len(pal) > longest_len:
                        longest_pal = pal
                        longest_len = len(pal)
                    
                    while (start >= 1) and (end < len(s)-1):
                        start -= 1
                        end += 1
                        
                        if s[start] == s[end]:
                            pal = s[start:end+1]
                            if len(pal) > longest_len:
                                longest_pal = pal
                                longest_len = len(pal)
                        else:
                            break
                
                # 2-letter palindrome base
                if s[i] == s[i+1]:
                    start = i
                    end = i+1
                    pal = s[start:end+1]
                    if len(pal) > longest_len:
                        longest_pal = pal
                        longest_len = len(pal)
                    
                    while (start >= 1) and (end < len(s)-1):
                        start -= 1
                        end += 1
                        
                        if s[start] == s[end]:
                            pal = s[start:end+1]
                            if len(pal) > longest_len:
                                longest_pal = pal
                                longest_len = len(pal)
                        else:
                            break
                
        return longest_pal
