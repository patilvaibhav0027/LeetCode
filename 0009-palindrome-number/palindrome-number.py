class Solution:
    def isPalindrome(self, n: int) -> bool:
        res=0
        x=n
        while x>0:
            rem=x%10
            res=res*10+rem
            x//=10 

        if res==n: 
            return True
        else :
            return False