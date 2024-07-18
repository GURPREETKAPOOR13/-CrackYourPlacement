from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_count_and_sort(nums, temp, left, right):
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = merge_count_and_sort(nums, temp, left, mid)
            count += merge_count_and_sort(nums, temp, mid + 1, right)
            count += merge_and_count(nums, temp, left, mid, right)
            
            return count
        
        def merge_and_count(nums, temp, left, mid, right):
            i, j = left, mid + 1
            count = 0
            while i <= mid and j <= right:
                if nums[i] > 2 * nums[j]:
                    count += (mid - i + 1)
                    j += 1
                else:
                    i += 1
            
            # Merge the two halves while sorting
            i, j, k = left, mid + 1, left
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            
            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1
            
            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1
            
            for i in range(left, right + 1):
                nums[i] = temp[i]
            
            return count
        
        # Edge case
        if not nums:
            return 0
        
        # Temporary array for merge sort
        temp = [0] * len(nums)
        
        # Call merge_count_and_sort to get the count of reverse pairs
        return merge_count_and_sort(nums, temp, 0, len(nums) - 1)
