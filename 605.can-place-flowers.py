#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i ==0 and (len(flowerbed) == 1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            if n <= 0:
                return True
        return False
    
# @lc code=end

# basic approch is to loop through the flowerbed  
        # and if the current plot is empty, check if the previous and next plots are empty
        # if they are, then plant a flower and decrase n by 1
        # if n<=0 return True, else return False
        # edge case1: if the len==1 and it's empty, then should plant a flower
        # edge case2: if the first plot is empty, and the second plot is empty, then should plant a flower at the first plot
        # edge case3: if the last plot is empty, and the second last plot is empty, then should plant a flower at the last plot


# let the number of flowers that can be planted be n
        # let the consecutive empty plots be c 
        # their relationship is (c-2)/2 = n when c is odd, and (c-1)/2 = n when c is even
        # how to get c?
        # if flowerbed[0] == 0, then c = 1
        # if flowerbed[0] == 1, then c = 0