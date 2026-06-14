
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_count = 1, 0

        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
        
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)

        for i in range(len(nums)):
            num = nums[i]
            if not num:
                res[i] = prod
            if not zero_count:
                res[i] = prod // nums[i]
        
        return res
