class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = {}
        for num in nums:
            if num not in r:
                r[num] = nums.count(num)
            if len(r) > k:
                lowest_num = min(r, key=r.get)
                del r[lowest_num]
        return list(r.keys())
            
        