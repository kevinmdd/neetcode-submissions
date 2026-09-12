class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            num_sum = numbers[i] + numbers[j]
            if num_sum == target:
                return [i+1, j+1]
            if (num_sum-target) < 0:
                i += 1
            else:
                j -= 1