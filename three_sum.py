#!/usr/bin/env python3

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res



def main():
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(s.threeSum(nums))


if __name__ == "__main__":
    main()
