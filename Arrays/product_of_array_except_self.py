#!/usr/bin/python3
# # -*- coding: utf-8 -*-
"""
238. Product of Array Except Self
Medium
16.8K
924
Companies

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Seek O(N) solution without using division. This means we can't just multiply all the numbers together and then divide by each number.

        We can use a left and right array to store the product of all the numbers to the left and right of the current index. Then we can multiply the two arrays together to get the final answer.
        """
        # n = len(nums)
        # left = [1]*n
        # right = [1]*n
        # for i in range(1,n):
        #     left[i] = left[i-1]*nums[i-1]
        # for i in range(n-2,-1,-1):
        #     right[i] = right[i+1]*nums[i+1]
        # return [left[i]*right[i] for i in range(n)]
        """
        O(1) space? Maybe we don't need to store all the products
        """
        n = len(nums)
        # first pass for preproducts
        output = [1]*n
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]

        # second pass for postproducts
        postprod=1
        for i in range(n-2, -1, -1):
            postprod *= nums[i+1]
            output[i] *= postprod
            
        return output

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_productExceptSelf(self):
        self.assertEqual(self.solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(self.solution.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])


if __name__ == '__main__':
    unittest.main()