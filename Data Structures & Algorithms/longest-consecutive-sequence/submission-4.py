class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0

        #check if i+1 exists in nums, if it does then add if to length
        # sort the nums
        #if next number == nums[i-1] + 1
        # count++ consec num
        # else if it's not then breaks the consec count
        # then if count != 0 add it to a list of consec nums
        # return the largest num in the list
        # if list empty return 0
        if not nums:
            return 0

        # nums.sort()
        # count = 1
        # maxLength = 1
        # length = []

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue # skip duplicates 

        #     if nums[i] == nums[i-1] + 1:
        #         count += 1
        #     else:
        #         count = 1 # reset count
            
        #     #which consectutive pattern is bigger
        #     maxLength = max(maxLength, count)

        # return maxLength

        #if num - 1 not in array
        # add it to the array and that is the start
        # else if the num below it exists then you add to the length
        
        count = 1
        seen = set(nums)
        max_length = 0

        for num in seen:
            if num - 1 not in seen: #find the start
                start = num
                count = 1 # reset
                
                while start + 1 in seen:
                    count += 1 #track how many consec
                    start += 1 #move to next num
                
                #once there is no next num
                # calculate the max length
                max_length = max(max_length, count)
                

        return max_length

            


        