class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #can't create any sets so no look ups
        # target = 7 -> 1,2,3,4
        # 1+ 4 >? target? no so go up to higher number
        # 2+4 >? target? no 
        test = 0
        left = 0
        right = len(numbers) - 1

        for i in range(0, len(numbers)):
            test = numbers[left] + numbers[right]
            
            if test < target:
                left += 1
            elif test > target:
                right -= 1
            elif test == target:
                return [left+1, right+1]