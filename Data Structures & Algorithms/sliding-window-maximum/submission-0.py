class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        start = 0
        for end in range(len(nums)):
            if end - start + 1 == k:
                window = nums[start:end+1]
                output.append(max(window))
                start += 1
        return output