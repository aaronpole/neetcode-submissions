class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, val in enumerate(nums):
            if target-val in complement:
                return [complement[target-val], i]
            else:
                complement[val] = i