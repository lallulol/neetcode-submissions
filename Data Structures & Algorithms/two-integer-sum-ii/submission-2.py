class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            internal_right = len(numbers)-1
            while left < internal_right:
                if numbers[left]+numbers[internal_right] != target:
                    internal_right-=1
                else:
                    return [left+1, internal_right+1]
            left+=1