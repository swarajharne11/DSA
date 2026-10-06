"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Difficulty: Medium
Topic: Two Pointers

Approach:
    The array is sorted, so use one pointer at each end.
    - If the sum equals target, return the 1-indexed positions.
    - If the sum is too large, move the right pointer left to reduce it.
    - If the sum is too small, move the left pointer right to increase it.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            current = numbers[i] + numbers[j]
            if current == target:
                return [i + 1, j + 1]
            elif current > target:
                j -= 1
            else:
                i += 1
