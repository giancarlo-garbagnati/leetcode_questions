""" https://leetcode.com/problems/zigzag-conversion/description/
6. Zigzag Conversion
Solved
Medium
Topics
premium lock icon
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

# Very frustrating problem with unclear sample cases.

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        if numRows >= len(s):
            return s
        if len(s) <= 1:
            return s

        arr = [[] for _ in range(numRows)] # create an array of arrays
        j = 0 # index tracker for when to switch to slant line
        k = 0 # index tracker for slant line
        zig = False

        for c in s:
            if numRows == 2: # different for numRows = 2
                if not zig:
                    arr[0].append(c)
                    zig = True
                else:
                    arr[1].append(c)
                    zig = False
            elif not zig:
                arr[j].append(c)
                j += 1
                if j >= numRows:
                    zig = True
                    j = 0
            else: 
                arr[numRows-k-2].append(c)
                k += 1
                if k >= numRows-2:
                    k = 0
                    zig = False

        result = ''
        for l in arr:
            result += ''.join(l)

        return result

        """
        A  C  
        B  D

        numRows = 3, middle = 1
        A   E
        B D F
        C   G

        numRows = 4, middle = 2
        A     G
        B   F H
        C E   I
        D     J

        ABCDEFGHIJKLMNO

        numRows = 6, middle = 4
        A         J
        B       I K
        C     H   L
        D   G     M
        E F       N
        F         O

        numRows = 5, middle = 3
        A       I
        B     H J
        C   G   K
        D F     L
        E       M
        """
