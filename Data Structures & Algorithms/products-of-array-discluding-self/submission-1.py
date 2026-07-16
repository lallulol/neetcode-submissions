class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = [1]*len(nums)
        for i in range(len(nums)):
            left_list = nums[:i]
            right_list = nums[i+1:]
            left_prod, right_prod = (1,1)
            for x in left_list:
                left_prod *= x
            for y in right_list:
                right_prod *= y
            new_list[i] = left_prod * right_prod
        return new_list    