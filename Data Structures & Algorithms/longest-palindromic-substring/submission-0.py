class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        start=0
        max_len=1
        def find_palindrome(left, right): # expand around the centre
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1

        for i in range(n):
            odd=find_palindrome(i,i)
            even=find_palindrome(i, i+1)
            length=max(odd,even)
            if length>max_len:
                max_len=length
                start=(i-(length-1)//2)
        return s[start:start+max_len]


        