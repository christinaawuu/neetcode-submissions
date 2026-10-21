class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        products = [1]*len(nums) #fill answer up with 1s

        #loop through nums and calculate prefix for first pass 
        #then multiply by suffix in the second pass
        # left = nums[0:i]
        # right = nums[i+1, n]
        for i in range(len(nums)):
            products[i] = prefix
            prefix *= nums[i]

        #loop backwards to calc suffix
        for i in range(len(nums)-1, -1, -1):
            products[i] *= suffix # you now multiply since missing last num
            suffix *= nums[i]

        return products