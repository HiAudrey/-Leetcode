

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, i in enumerates(nums):
            #计算减数
            rem = target - i
            #如果减数在列表里，就输出这俩数
            if rem in nums and nums.index(rem) != index1:
                return [index1, nums.index(rem)]
            else:
                continue