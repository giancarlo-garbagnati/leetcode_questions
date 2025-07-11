""" https://leetcode.com/problems/two-sum/
1. Two Sum
Solved
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_dict = {}
        for i, num in enumerate(nums):
            if target-num in nums_dict.keys():
                return [nums_dict[target-num], i]
            elif num in nums_dict.keys():
                continue
            else: # add new item to dict
                nums_dict[num] = i

        # I thought about using pointers on each end, but the list would
        # need to be sorted

    """ brute force (O(n^2) soln)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j <= i:
                    continue
                elif nums[i] + nums[j] == target:
                    return [i,j]
    """

        

"""
Test cases:
Case 1:
Input
nums =
[2,7,11,15]
target =
9
Output
[0,1]
Expected
[0,1]

Case 2:
Input
nums =
[3,2,4]
target =
6
Output
[1,2]
Expected
[1,2]

Case 3:
Input
nums =
[3,3]
target =
6
Output
[0,1]
Expected
[0,1]
"""
