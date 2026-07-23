from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = deque()
        start = 0
        for end in range(len(nums)):
            while dq and nums[dq[-1]] < nums[end]:
                dq.pop()
            dq.append(end)
            if dq[0] <= end -k:
                dq.popleft()
            if end - start + 1 == k:
                window = nums[start:end+1]
                output.append(nums[dq[0]])
                start += 1
        return output