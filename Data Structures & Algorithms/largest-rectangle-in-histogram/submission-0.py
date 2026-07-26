class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i in range(len(heights)+1):
            curHeight = heights[i] if i < len(heights) else 0
            while stack and heights[stack[-1]] > curHeight:
                height = stack.pop()
                left_boundry = stack[-1]+1 if stack else 0
                right_boundry = i
                area = (right_boundry-left_boundry)*heights[height]
                maxArea = max(area, maxArea)
            stack.append(i)
        return maxArea