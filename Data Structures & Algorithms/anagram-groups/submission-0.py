class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) # mapping the count of chars to list of anagrams
        for s in strs:
            count = [0] * 26 # for a - z
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())
