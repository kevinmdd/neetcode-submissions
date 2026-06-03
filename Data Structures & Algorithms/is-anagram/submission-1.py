class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        anagram = False
        if (len(s) == len(t)):
            for i in range(len(s)):
                if(s[i] == t[i]):
                    anagram = True
                else:
                    anagram = False
                    break
                
        return anagram
