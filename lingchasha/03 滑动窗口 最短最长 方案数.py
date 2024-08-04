# LeetCode 209 
# 长度最小的子数组 给定一个含有n个正整数和一个正整数target
# target = 7 长度最小为 target 的连续数组

from typing import List
from collections import Counter

class solution:
    def minSubArrayLen(self,target:int,nums:List[int]) -> int:
        n = len(nums)
        ans = n+1
        s = 0
        left = 0
        for right,x in enumerate(nums):
            s += x
            while s - nums[right] >= target:
                s -= nums[left]
            if s>= target:
                ans = min(ans,right-left+1)
        return ans if ans <= n else 0
    
    def minSubArrayLen1(self,target:int,nums:List[int]) -> int:
        n = len(target)
        left = 0
        right  = n
        ans = n + 1 # inf
        s = 0

        for right,x in enumerate(nums):
            s += x
            while s >= target:
                ans = min(ans,right - left + 1)
                s -= nums[left]
                left += 1

        return ans if ans <= n else 0

        

    # Leetcode 713 乘积小于K的子数组，
    # 返回子数组内所有元素的乘积和严格小于k的连续数组的数目
    def numSubArrayProductLessThank(self,nums:List[int],k:int)->int:
        if k <= 1:
            return 0
        ans = 0
        prod = 1
        left = 0
        for right,x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
        
    #Leetcode 3 无重复字符的最长子串
    def lengthOfLongestSubstring(self,s:str) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right,c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans

