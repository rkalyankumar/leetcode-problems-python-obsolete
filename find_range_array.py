#!/usr/bin/python3

from typing import List


"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

import bisect

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_pos = self.search(nums, target, True)
        if first_pos == -1:
            return [-1, -1]
        second_pos = self.search(nums, target, False)
        return [first_pos, second_pos]

    def search(self, nums, target, first_occurence = True):
        # Do a binary search
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                if first_occurence:
                    if mid == left or nums[mid - 1] != target:
                        return mid
                    right = mid  - 1
                else:
                    if mid == right or nums[mid + 1] != target:
                        return mid
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

def main():
    nums = [5,7,7,8,8,10]
    target = 8
    s = Solution()
    print(s.searchRange(nums, target))


if __name__ == "__main__":
    main()
