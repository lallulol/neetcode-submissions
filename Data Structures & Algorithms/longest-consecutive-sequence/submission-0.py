class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = sorted(list(set(nums)))
        longest = 1
        current = 1
        for i in range(len(nums) - 1):
             if nums[i+1] == nums[i] + 1:
                current+=1
             else:
                longest = max(longest, current)
                current = 1
        return max(longest, current)