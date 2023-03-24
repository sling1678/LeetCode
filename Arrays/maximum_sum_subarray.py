#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
53. Maximum Subarray
Medium
28.8K
1.3K
Companies
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        We are looking for consecutive items that add up to the maximum. Best to think in terms of: what is the best sum we can get if array ended at the current index i. The logic will be: either we extend the current sum or start a new subarray. If we find that including the current item a[i] to current_subarray_sum makes it negative, then of course we should stop this current subarray and start a new one by skipping; we do skipping by resetting the current_subarray_sum to zero. At each stage, we keep track of best sum obtained so far and the index it ended at.

        """
        best_sum_and_index = [nums[0], 0]
        current_subarray_sum = 0
        for i in range(len(nums)):
            current_subarray_sum += nums[i] # extend the current subarray
            if current_subarray_sum > best_sum_and_index[0]:
                best_sum_and_index = [current_subarray_sum, i]
            if current_subarray_sum < 0:
                current_subarray_sum = 0 # reset the current subarray sum
        return best_sum_and_index[0]

import unittest
class TestMaxSubArray(unittest.TestCase):
    def test_maxSubArray(self):
        self.assertEqual(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(Solution().maxSubArray([1]), 1)
        self.assertEqual(Solution().maxSubArray([5,4,-1,7,8]), 23) 
        self.assertEqual(Solution().maxSubArray([-2,1]), 1)
        self.assertEqual(Solution().maxSubArray([-2,-1]), -1)
        self.assertEqual(Solution().maxSubArray([-2,-1,-3]), -1)
        self.assertEqual(Solution().maxSubArray([-2,-1,-3,-4]), -1)
        self.assertEqual(Solution().maxSubArray([-2,-1,-3,-4,-5]), -1)

if __name__ == '__main__':
    unittest.main()
    