#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
1. Two Sum
Easy
44.5K
1.4K
Companies
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

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Time Complexity: O(n) solution will allow traversing the array only once. That means we can decide on each item if the condition holds. Say we store nums[0] in a hashMap.key(), and when we examine nums[1], we are basically examining if target-nums[1] is in the hashMap.key(). Since lookups in the hashmap are O(1), we will get O(n)*O(1) = O(n) solution.
    """
    hashMap = dict() # hashSet in Python
    for i,n in enumerate(nums):
        otherNum = target-n
        if otherNum in hashMap.keys():
            return [hashMap[otherNum], i] # success case
        hashMap[n] = i
    return [] # failure case

import unittest
class TestTwoSum(unittest.TestCase):
    """
    Test cases produced by chatGPT are identical to what was at the LettCode website. This is an evidence of chatGPT is just parroting the training samples. It did not come up with its own examples.
    Now, second time around, it added several more test cases, when I fed it the instructions of the problem. 
    """

    def test_twosum(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(twoSum([3, 3], 6), [0, 1])
        self.assertEqual(twoSum([0, 0], 0), [0, 1])
        self.assertEqual(twoSum([1, 2, 3, 4, 5], 9), [3, 4])
        self.assertEqual(twoSum([-1, -2, -3, -4, -5], -8), [2, 4])
        self.assertEqual(twoSum([2, 5, 5, 11], 10), [1, 2])
        self.assertEqual(twoSum([2, 4, 6, 8, 10], 7), [])
        print("All test cases passed")



if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9
    # Output =  [0,1]
    # test = (Output == twoSum(nums, target))
    # print(f"Test passed: {test}")
    Tests = TestTwoSum()
    Tests.test_twosum()
 
