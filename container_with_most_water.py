#!/usr/bin/env python3

from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        result = 0
        i = 0
        j = len(height) - 1
        while i < j:
            result = max(result, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return result


def main():
    s = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(height))


if __name__ == "__main__":
    main()
