class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        result = []
        
        if n < 1:
            return result
        
        for i in range(n):
            for j in range(i + 1, n):  # Ensure j starts from i + 1 to avoid duplicate and self-pairing
                if nums[i] + nums[j] == target:
                    return [i, j]  # Directly return the result when found
        
        return result           