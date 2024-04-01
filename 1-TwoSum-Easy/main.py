class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #val:index

        for i, value in enumerate(nums):
            diff = target - value 
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[value] = i

        
