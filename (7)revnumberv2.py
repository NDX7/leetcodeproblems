class Solution(object):
    def reverse(self, x):
        if x>0:
            x=str(x)
            rx=x[::-1]
            rx=int(rx)
            return(rx)
        else:
            x=abs(x)
            x=str(x)
            rx=x[::-1]
            rx=int(rx)
            return(0-rx)
            
        
        
