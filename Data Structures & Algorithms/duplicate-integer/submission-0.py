class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()
        for i in nums:
            if i in dup_set:
                return True
            else:
                dup_set.add(i)

        return False