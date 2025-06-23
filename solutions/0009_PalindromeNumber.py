"""
9. Palindrome Number
Easy

Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0: # negatives should return false
            return False
        
        # convert to string and pointers for traversing
        s = str(x)
        l = 0
        r = len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True



""" # My in progress attempt to do it without converting to string. It was taking longer than I'd liked and wanted to move on
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # need a function to check if decimal point is in the middle
        # then if that's the case, figure out how to convert the decimal to int (multiplying by some factor of 10)

        if x < 0: # negatives should return false
            return False
        # elif x % 1 != 0: # 
        #     while x % 1 != 0:
        #         x *= 10
        #     x = int(x)
        elif (isinstance(x, int)) and (x < 10): # might not work with decimal points
            return True

        l = []
        lr = []
        y = x
        before_decimal = 0
        after_decimal = 0
        over_one = True
        while y > 0:
            ones_digit = y % 10




"""
