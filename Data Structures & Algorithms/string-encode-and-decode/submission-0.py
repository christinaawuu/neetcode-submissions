class Solution:

    def encode(self, strs: List[str]) -> str:
        #label each str in the list by length, seperator, and then word
        # hi -> 2#hi so it only reads the next two characters as one str
        coded = ""

        for s in strs:
            length = len(s)
            coded += str(length) + "#" + s
        return coded


    def decode(self, s: str) -> List[str]:
        #2#hi -> read the number until you hit the # and then read for that amount of chars 
        decoded = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1 # skip the #
            # for the length of the word, add it to a string and then add it to the list
            length = int(s[i:j]) # convert string to int
            
            # beginning of the word to end j+1 to skip the #
            word = s[j + 1 : j + 1 + length]
            i = j+1+length # end of the word

            # i += 1 #skip the seperator index
            # for l in length:
            #     word += s[i] # loop to the next word
            # i += length # skip to the next word
            decoded.append(word) 
            

        return decoded











