class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1