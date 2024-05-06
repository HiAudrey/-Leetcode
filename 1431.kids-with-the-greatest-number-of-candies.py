#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        result = list()
        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                result.append(1)
            else:
                result.append(0)
        return result  
# @lc code=end

