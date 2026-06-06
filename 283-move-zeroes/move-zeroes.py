from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroFoundAt = 0
        
        # Step 1: Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        
        # Step 2: Fill remaining places with zero
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
