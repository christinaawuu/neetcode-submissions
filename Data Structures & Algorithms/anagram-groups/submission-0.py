class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #base case if theres only one item in the string
        if len(strs) == 1:
            return [strs]

        # iterate through strs and put the string in a list of seen
        # if not then add it to the seen list
        # if it is add that string to the list of strings

        order = {} #hashmap, {alphabetical, words} order[aet] = {eat, tea,}
        for word in strs:
            # sort the word in alphabetical order 
            alpha = "".join(sorted(word))
            
            if alpha not in order:
                order[alpha] = [word] #create a new list []
            else: 
                order[alpha].append(word) #add the word to the list 

        #put it in a list to match return type
        return list(order.values())

