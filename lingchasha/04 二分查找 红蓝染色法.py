#leetcode 34,在排序数组中 查找元素的第一个和最后一个位置
# 【5,7,7,8,8,10】 target 8 => 3,4
from typing import List

def lower_bound(nums:List[int],target:int) -> int:
    left = 0
    right = len(nums) 
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid  + 1
        else:
            right = mid
    return left

class Solution:
    @staticmethod
    def searchRange(nums:List[int],target:int) -> List[int]:
        start = lower_bound(nums,target)
        print(start)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        end = lower_bound(nums,target + 1) - 1
        print(end)
        return [start,end]

mylist = [5,7,7,7,8,8,8,8,10]
print(lower_bound(mylist,8))
Solution.searchRange(nums=mylist,target=8)