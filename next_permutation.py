#!/usr/bin/env python3

from typing import List

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.


Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:

Input: nums = [1]
Output: [1]

"""

class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Input: nums = [1,2,3]
        Output: [1,3,2]
        """
        inversion_point = len(nums) - 2
        while inversion_point >= 0 and \
            nums[inversion_point] >= nums[inversion_point + 1]:
            inversion_point -= 1
        if inversion_point  > 0:
            for i in reversed(range(inversion_point + 1, len(nums))):
                if nums[i] > nums[inversion_point]:
                    nums[i], nums[inversion_point] =  \
                        nums[inversion_point], nums[i]
                    break
        nums[inversion_point + 1: ]= reversed(nums[inversion_point + 1: ])


def main():
    s = Solution()
    nums = [1, 2, 3]
    print('Input: ', nums)
    s.nextPermutation(nums)
    print('Next permutation: ', nums)
    nums = [1,1,5]
    s.nextPermutation(nums)
    print('Next permutation: ', nums)

    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print('Next permutation: ', nums)


if __name__ == "__main__":
    main()
