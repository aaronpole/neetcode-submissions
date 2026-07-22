class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        set_nums = set(nums)
        for i in set_nums:
            if i-1 in set_nums:
                continue
            current = i
            length = 1
            while current+1 in set_nums:
                current+=1
                length+=1
            if length > max_length:
                max_length = length
        return max_length