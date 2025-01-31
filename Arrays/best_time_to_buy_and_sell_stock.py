#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
121. Best Time to Buy and Sell Stock
Easy
24.3K
759
Companies

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

NOTE: This is a follow-up problem to Best Time to Buy and Sell Stock. The only difference is that you are now allowed to complete at most two transactions.
NOTE: This is a follow-up problem to Best Time to Buy and Sell Stock. The only difference is that you are now allowed to complete at most k transactions.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Assuming only ONE transaction is allowed. We can get O(n) solution by computing the most profit we will obtain if we sold that day. Of course we can sell only from day 2 onward with index 1 being day 2.
        """

        # this is not needed since for loop below will already take care of this case.
        # if len(prices) <= 1:
        #   return 0

        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i]) #so far the lowest price
            maxProfit = max(maxProfit, prices[i]-minPrice) # so far the highest profit
        return maxProfit

import unittest
class TestMaxProfit(unittest.TestCase):
    def test_maxProfit(self):
        prices = [7,1,5,3,6,4]
        self.assertEqual(Solution().maxProfit(prices), 5)
        prices = [7,6,4,3,1]
        self.assertEqual(Solution().maxProfit(prices), 0)

if __name__ == "__main__":
    unittest.main()



