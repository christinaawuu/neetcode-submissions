class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort and make a counter for each number
        #[key, val] -> [int, frequency]
        # for k, see which one's have the highest frequency

        counter = {}
        for num in nums:
            if num in counter: #increase int count
                counter[num] += 1
            else: 
                counter[num] = 1 # add it to the dict/ hashmap

        #sort the values of the counter from most tto least (item[1] is the val)
        sorted_nums = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        sorted_nums[:k] #splice the list to get k elements
        # sorted_items = [(num, freq), (num, freq), ...]

        top = []
        for i in range(k):
            top.append(sorted_nums[i][0]) #add the key 

        return top