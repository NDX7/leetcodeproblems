class Solution(object):
    def reverse(self, x):
        n=len(str(x))
        rev=0
        if x>0:
            for i in range(n):
                num=x%10
                x=x//10
                rev=rev*10+num
            if rev<2147483647:
                return rev
            else:
                return 0
            
        else:
            x=abs(x)
            n=len(str(x))
            for i in range(n):
                num=x%10
                x=x//10
                rev=rev*10+num
            if rev<2147483647:
                return 0-rev
            else:
                return 0
            
