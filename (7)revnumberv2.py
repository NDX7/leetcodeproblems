class Solution(object):
    def reverse(self, x):
        if x > 0:
            x = str(x)
            rx = x[::-1]
            rx = int(rx)
            
            
            if rx > 2147483647:
                return 0
            return rx
        else:
            x = abs(x)
            x = str(x)
            rx = x[::-1]
            rx = int(rx)
            final_rx = 0 - rx
            
            
            if final_rx < -2147483648:
                return 0
            return final_rx
