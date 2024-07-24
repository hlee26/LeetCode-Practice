class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ n = len(nums) 
        out = []
        for i in range(0,n):
            total = 1
            for j in range(0,n):
                if j is not i:
                    total = total*nums[j]
            out.append(total)
        return out """
        n = len(nums)
        out = [1] * n
        
        left = 1
        for i in range(n):
            out[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(n-1, -1, -1):
            out[i] *= right
            right *= nums[i]
        
        return out