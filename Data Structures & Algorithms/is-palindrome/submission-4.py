class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        sChar = list(s.replace(" ", ""))
        palin = True
        ascii = "01234567890abcdefghijklmnopqrstuvwxyz"
        start = 0
        end = len(sChar) - 1
        if (end == 1):
            if (sChar[start] in ascii and sChar[end] in ascii):
                if (sChar[start] != sChar[end]):
                    palin = False
            else:
                palin = True
                
        while(start < end and end != 1):
            if (sChar[start] not in ascii):
                start += 1
            if (sChar[end] not in ascii):
                end -= 1
            else:
                if (sChar[start] != sChar[end]):
                    palin = False
                    break
                else:
                    start += 1
                    end -= 1
        return palin
            

