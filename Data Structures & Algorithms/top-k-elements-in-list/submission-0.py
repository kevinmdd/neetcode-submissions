class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = {}
        i = []
        c = 0
        for num in nums:
            if num not in r:
                num_count = nums.count(num)
                r[num] = num_count
                if len(r) > k:
                    lowest_num = min(r, key=r.get)
                    del r[lowest_num]
        return list(r.keys())
            
        