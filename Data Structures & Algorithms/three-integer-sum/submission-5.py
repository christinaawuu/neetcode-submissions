class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i+j+k=0 -> i = -(j+k)
        # sort the nums list
        # do 2sum on the numbers to the right of i
        # index = 0
        # left = nums[index+1]
        # right = nums[nums.size()]

        trios = []
        index = 0
        nums.sort()

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # skip duplicates

            left = i+1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                test = nums[left] + nums[right]
                
                if test < target:
                    left += 1
                elif test > target:
                    right -= 1
                elif test == target:
                    trios.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate second and third values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return trios
        