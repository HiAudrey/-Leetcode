def twoSum(nums, target):
    record = dict() # define a hash table

    for index, value in enumerate(nums):
        if target - value in record:
            return (record[target - value], index)
        else:
            record[value] = index
    return []

nums = [4,2,3,8,5]
target = 9
print(twoSum(nums, target))

class Solution():
    def twoSum(nums, target):
        record = dict()
        for index, val in enumerate(nums):
            if target - val in record:
                return (record[target - val], index)
            record[val] = index

print(Solution.twoSum(nums, target))