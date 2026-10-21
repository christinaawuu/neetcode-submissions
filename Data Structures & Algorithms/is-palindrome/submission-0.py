class Solution:
    def isPalindrome(self, s: str) -> bool:
        #make it a string without spaces
        #check if i == (size - 1) and keep going till the center

        noSpaces = ''.join(char.lower() for char in s if char.isalnum())
        size = len(noSpaces) - 1

        for i in range(0, len(noSpaces)):
            # when you reach the middle
            if i > size: 
                break

            if noSpaces[i] == noSpaces[size]:
                size -= 1
            else:
                return False

        return True