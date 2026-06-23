class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range (0,n):
            
            for j in range(i+1,n):
                n1=nums[i]
                n2=nums[j]
                if n1+n2==target:
                    return i,j
                    
