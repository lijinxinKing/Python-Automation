# leetcode 167 two num sum
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1
                
    #LeetCode 15 three num sum
    def thresSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        ans = []
        n = len(numbers)
        for i in range(n - 2):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                s = numbers[i] + numbers[left] + numbers[right]
                
                if s == target:
                    return [i + 1, left + 1, right + 1]
                elif s < target:
                    left += 1
                else:
                    right -= 1

# 写测试用例
