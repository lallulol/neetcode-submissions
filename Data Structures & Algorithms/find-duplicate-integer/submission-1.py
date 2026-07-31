class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = {}
        for i in nums:
            if i in counter:
                return i
            else:
                counter[i] = 1