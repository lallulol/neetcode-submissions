class Solution:
    def trap(self, height: List[int]) -> int:
        total_amount = 0
        left, right = 0, len(height)-1
        left_max, right_max = 0,0
        while left < right:
            if height[left]<height[right]:
                if height[left]>left_max:
                    left_max=height[left]
                else:
                    total_amount+=left_max-height[left]
                left+=1
            else:
                if height[right]>right_max:
                    right_max=height[right]
                else:
                    total_amount+=right_max-height[right]
                right-=1
        return total_amount