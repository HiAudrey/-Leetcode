#https://leetcode.com/problems/two-sum/
import pandas as pd
from collections import Counter

def twoSum(nums, target):
    dic = dict()
    print(dic)
    for i, val in enumerate(nums):
        if target - val in dic:
            return [i, dic[target - val]]
        else:
            dic[val] = i
            print(dic)

#nums = [3,3,1,9,4]
nums = [4,2,5,3,8]
target = 9
print(twoSum(nums, target))
print(list(enumerate(nums)))

