#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # store vowels in a set
        vowels = set('aeiouAEIOU')
        # convert string to list
        s = list(s)
        # set left and right pointers
        left, right = 0, len(s) - 1
        
        # loop until left pointer is less than right pointer
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
        
        # convert list to string
        return ''.join(s)
        
# @lc code=end

