class Solution(object):
    def isPalindrome(self, x):
        xs=str(x)
        xs=xs[::-1]
        if xs==str(x):
            return(True)
        else:
            return(False)
