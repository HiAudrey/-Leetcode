#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        result = []
        if len(w1) > len(w2):
            for i in range(len(w2)):
                result.append(w1[i])
                result.append(w2[i])
            return ''.join(result) + ''.join(w1[len(w2):]) + ''.join(w2[len(w1):])
        elif len(w1) < len(w2):
            for i in range(len(w1)):
                result.append(w1[i])
                result.append(w2[i])
            return ''.join(result) + ''.join(w1[len(w2):]) + ''.join(w2[len(w1):])
        else:
            for i in range(len(w1)):
                result.append(w1[i])
                result.append(w2[i])
        return ''.join(result)
# @lc code=end

