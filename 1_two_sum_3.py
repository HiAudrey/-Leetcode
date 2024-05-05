class Solution:
    def twoSum(nums, target):
        records = dict()
        for index, value in enumerate(nums):
            print('现在在搞这个元素', index, value, target - value)
            if target - value in records:   # 遍历当前元素，并在map中寻找是否有匹配的key
                print('有记录', records)
                return [records[target- value], index]  #返回map里的value 和array里的index
            records[value] = index    # 如果没找到匹配对，就把访问过的元素和下标加入到map中
            print('搞完这个元素后的hashmap', records)
        return []

nums = [4,2,3,8,5]
target = 9
print(Solution.twoSum(nums, target))