class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack =[]
        max_area = 0
        for i in range(len(heights)):
            area = 0
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                right_bound = i
                left_bound = stack[-1] if stack else -1
                width = right_bound - left_bound - 1
                area = heights[index] * width
                max_area = max(area,max_area)
            stack.append(i)
        return max_area
