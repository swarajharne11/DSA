"""
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/

Difficulty: Medium
Topic: Sliding Window

Approach:
    Find the longest subarray containing at most 2 distinct fruit types.
    - Expand the window by moving `right` and counting each fruit in a dict.
    - If the window has more than 2 types, shrink from `left` until it
      has 2 again, removing a type from the dict when its count hits 0.
    - After each step, update the best window length.

Time:  O(n)
Space: O(1)  (the dict never holds more than 3 keys)
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        best = 0
        left = 0

        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right], 0) + 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1

            best = max(best, right - left + 1)

        return best
