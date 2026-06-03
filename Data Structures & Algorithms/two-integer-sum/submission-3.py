class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSummed = []
        breaks = False
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    twoSummed.append(i)
                    twoSummed.append(j)
                    breaks = True
                    break
            if (breaks):
                break
        return twoSummed