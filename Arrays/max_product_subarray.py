#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
152. Maximum Product Subarray
Medium
15.5K
467
Companies
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        The basic observation is that maxPositive * negative turns into minNegative and minNegative * negative turns into maxPositive. For postive current item, the switch does not occur
        """
        maxPositive = minNegative = bestProduct = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if n < 0:
                maxPositive, minNegative = minNegative, maxPositive
            
            maxPositive = max(n, maxPositive * n)
            minNegative = min(n, minNegative * n)

            bestProduct = max(bestProduct, maxPositive, minNegative)
        return bestProduct

import unittest
class TestMaxProduct(unittest.TestCase):
    def test_maxProduct(self):
        self.assertEqual(Solution().maxProduct([2,3,-2,4]), 6)
        self.assertEqual(Solution().maxProduct([-2,0,-1]), 0)
        self.assertEqual(Solution().maxProduct([-2,3,-4]), 24)
        self.assertEqual(Solution().maxProduct([-2]), -2)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4,0]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4,0,1]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4,0,1,-2]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4,0,1,-2,3]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4,0,1,-2,3,-4]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4,0,1,-2,3,-4,0]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4,0,1,-2,3,-4,0,1]), 24)
        self.assertEqual(Solution().maxProduct([-2,3,-4,0,1,-2,3,-4,0,1,-2,3,-4,0,1,-2]), 24)
    
if __name__ == "__main__":
    unittest.main()