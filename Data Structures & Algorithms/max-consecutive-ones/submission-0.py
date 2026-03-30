class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest_count = 0
        one_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                one_count += 1
                if (one_count > highest_count):
                    highest_count = one_count
            else:
                one_count = 0
        return highest_count



        