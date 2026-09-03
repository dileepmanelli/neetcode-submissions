class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls={}
        left=0
        length=0
        for right in range(len(s)):
            if s[right] in ls and ls[s[right]]>=left: #
                left=ls[s[right]]+1

            ls[s[right]]=right # last seen
            if right-left+1>length:   
                length=right-left+1
        return length    