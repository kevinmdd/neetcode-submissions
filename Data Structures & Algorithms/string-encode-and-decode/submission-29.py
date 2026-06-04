class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        if not strs:
            return encoded
        for i in range(len(strs)):
            string_length = str(len(strs[i])).rjust(3, '0')
            encoded += "#" + string_length + strs[i]
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded = []
        if len(s) <= 3:
            decoded.append(s[2:])
            return decoded
        i = 0
        j = len(s)
        while i < j:
            # if pattern is # and next is a number
            if s[i] == "000" and s[i-1] == "#":
                decoded.append("")
            elif s[i-1] == "#" and s[i].isdigit():
                string_length = s[i] + s[i+1] + s[i+2]
                length = int(string_length) + i + 3
                decode = s[i+3: length]
                decoded.append(decode)
                i = length
            else:
                i += 1
        return decoded