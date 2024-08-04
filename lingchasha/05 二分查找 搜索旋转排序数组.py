#Leetcode 162 寻找峰值，峰值元素是指其值严格大于左右林值的元素
# nums [1,2,3,1] 2 3
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
                # nums [1,2,3,1] 2 3
                # mid = 1, nums[mid] = 2, nums[mid + 1] = 3, nums[mid] < nums[mid + 1], left = mid + 1 = 2, right = 2
                # mid = 2, nums[mid] = 3, nums[mid + 1] = 1, nums[mid] > nums[mid + 1], right = mid = 2, left = 2
            else:
                right = mid
                # nums [1,2,3,1] 2 3
        return left

    # LeetCode 153 寻找旋转排序数组中的最小值
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1            
        return nums[left]
    
# 测试用例

# nums [1,2,3,1] 2 3
# nums [1,2,3,1] 1 0

    #Leetcode 33 搜索旋转排序数组，假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    # nums [4,5,6,7,0,1,2] target = 0
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] < target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1           
        return -1


