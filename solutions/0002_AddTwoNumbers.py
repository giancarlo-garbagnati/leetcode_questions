""" https://leetcode.com/problems/add-two-numbers/description/
2. Add Two Numbers
Solved
Medium
Topics
premium lock icon
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:
2->4->3
5->6->4
-------
7->0->8

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        snum1 = str(l1.val)
        while l1.next:
            l1 = l1.next
            snum1 = str(l1.val) + snum1

        snum2 = str(l2.val)
        while l2.next:
            l2 = l2.next
            snum2 = str(l2.val) + snum2
        
        result_snum = str(int(snum1) + int(snum2))
        
        for i, c in enumerate(result_snum):
            if i == 0: # and len(result_snum) == 1:
                result = ListNode(int(c))
            else:
                result = ListNode(int(c), result)

        return result

"""
Test Cases:

Case 1:
Input
l1 =
[2,4,3]
l2 =
[5,6,4]
Output
[7,0,8]
Expected
[7,0,8]

Case 2:
Input
l1 =
[0]
l2 =
[0]
Output
[0]
Expected
[0]

Case 3:
Input
l1 =
[9,9,9,9,9,9,9]
l2 =
[9,9,9,9]
Output
[8,9,9,9,0,0,0,1]
Expected
[8,9,9,9,0,0,0,1]
"""
