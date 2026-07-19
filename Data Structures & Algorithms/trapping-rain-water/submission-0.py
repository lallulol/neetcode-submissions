class Solution:
    def trap(self, height: List[int]) -> int:
        total_amount = 0
        for i in range(1, len(height)-1):
            total_amount += max(min(max(height[:i]), max(height[i:]))-height[i],0)
        return total_amount