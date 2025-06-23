""" https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # function to remove the highest and lowest values from 2 sorted arrays
        def remove_high_and_low(x,y):
            if len(x) == 0:
                y.pop()
                y.pop(0)
                return x, y
            elif len(y) == 0:
                x.pop()
                x.pop(0)
                return x, y
            else:
                # remove highest
                if x[-1] == y[-1]:
                    if len(x) > len(y):
                        x.pop()
                    else:
                        y.pop()
                elif x[-1] > y[-1]:
                    x.pop()
                else:
                    y.pop()
                # remove lowest
                if len(x) == 0:
                    y.pop(0)
                elif len(y) == 0:
                    x.pop(0)
                elif x[0] == y[0]:
                    if len(x) > len(y):
                        x.pop(0)
                    else:
                        y.pop(0)
                elif x[0] < y[0]:
                    x.pop(0)
                else:
                    y.pop(0)
                return x, y

        iterations = int( (len(nums1) + len(nums2) - 1) / 2 )

        for _ in range(iterations):
            nums1, nums2 = remove_high_and_low(nums1, nums2)

        total = nums1 + nums2
        total[0] = total[0]*1.0
        median = sum(total)/len(total)

        return median
