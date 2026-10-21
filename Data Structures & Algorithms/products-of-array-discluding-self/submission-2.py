class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        products = [1] * len(nums) #fill answer up with 1s
        #[1,1,1,1]

        #loop through nums and calculate prefix for first pass 
        #then multiply by suffix in the second pass
        
        #prefix starts with 1 and then you calulate prefix for the next iteration
        for i in range(len(nums)): # have to do this for the indexes
            products[i] *= prefix
            prefix *= nums[i]

        #loop backwards to calc suffix (4-1, -1(to get to 0 index), -1 decrement)
        for i in range(len(nums)-1, -1, -1):
            products[i] *= suffix # you now multiply since missing last num
            suffix *= nums[i]

        return products