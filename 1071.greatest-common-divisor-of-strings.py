#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # helper function to calculate the greatest common divisor
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
        
        # check if str1 + str2 is equal to str2 + str1
        if str1 + str2 != str2 + str1:
            return ""  # if not equal, return an empty string
        else:
            # call the gcd function to calculate the length of the greatest common divisor
            gcd_length = gcd(len(str1), len(str2))
            # return the substring with length gcd_length
            return str1[:gcd_length]



# @lc code=end

