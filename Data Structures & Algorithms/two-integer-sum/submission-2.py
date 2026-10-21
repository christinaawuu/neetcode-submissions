class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # base case if theres only two ints
        if len(nums) == 2:
            return [0,1]
        
        seen = {} # hashmap key value (int, index)

        # num2 = target - i (int searching for)
        # if the num hasn't been seen before 
            # return i and index of add
        for index, value in enumerate(nums):
            num2 =  target - nums[index] # 9 - 7 
            if num2 in seen:
                #return the index (seen, i)
                return [seen[num2], index]
            else:
                seen[value] = index # add value, index to map

        return []
            
