#!/usr/bin/env python3

from typing import List

class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
    	nums.sort()
    	result = nums[0] + nums[1] + nums[len(nums) - 1]
    	for i in range(len(nums) - 2):
    		left = i + 1
    		right = len(nums) - 1

    		while left < right:
    			sum = nums[i] + nums[left] + nums[right]

    			if sum == target:
    				return target

    			if sum > target:
    				right -= 1
    			elif sum < target:
    				left += 1


    			if abs(sum - target) < abs(result - target):
    				result = sum
    	return result


def main():
    s = Solution()
    nums = [-1,2,1,-4]
    print(s.threeSumClosest(nums, 1))


if __name__ == "__main__":
    main()
