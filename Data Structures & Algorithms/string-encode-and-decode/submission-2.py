class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for i in strs:
            final_str += i+"*#"+str(len(i))+"#"
        return final_str
    def decode(self, s: str) -> List[str]:
        final_list = []
        for i in range(len(s)):
            if s[i:i+2] == "*#":
                j = i + 2
                while s[j] != "#":
                    j += 1
                length = int(s[i+2:j])
                final_list.append(s[i-length:i])
        return final_list