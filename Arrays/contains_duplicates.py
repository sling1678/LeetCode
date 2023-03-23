#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
217. Contains Duplicate
Easy
8.6K
1.1K
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109

"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        In python, this is simple using a set data structure. Just place elements in a set as you traverse the list. If you encounter an element that is already in the set, then you have a duplicate.
        """
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

import unittest    
class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_contains_duplicate_true(self):
        self.assertEqual(self.s.containsDuplicate([1, 2, 3, 1]), True)
        self.assertEqual(self.s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)

    def test_contains_duplicate_false(self):
        self.assertEqual(self.s.containsDuplicate([1, 2, 3, 4]), False)

    def test_contains_duplicate_empty(self):
        self.assertEqual(self.s.containsDuplicate([]), False)

if __name__ == '__main__':
    unittest.main()

