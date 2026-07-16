class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    new_list[i]*=nums[j]
        return new_list