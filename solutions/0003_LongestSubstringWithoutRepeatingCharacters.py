""" https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
3. Longest Substring Without Repeating Characters
Medium
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

""" My original solution """
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0

        longest = 1

        if len(s) == 1:
            return longest

        for i, c in enumerate(s):
            l = []
            for c2 in s[i:]:
                if c2 not in l:
                    l.append(c2)
                else: # c2 in l
                    break
            if len(l) > longest:
                longest = len(l)

        return longest

""" Not my solution/algorithm, but my implementation of someone else's """

class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        longest = 0
        last_seen = {}
        l = 0

        for i, c in enumerate(s):
            if c in last_seen:
                l = max(l, last_seen[c] + 1)
            last_seen[c] = i
            longest = max(longest, i - l + 1)
            
        return longest
