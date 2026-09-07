class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) 
        i = 0 
        j = n-1
        max_water = 0
        while i < j:
            height_min = min(heights[i],heights[j])
            area = height_min * (j-i)
            max_water = max(max_water,area)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return max_water



        