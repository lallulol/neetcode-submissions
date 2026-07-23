class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        target = {}
        have = 0
        start = 0
        best_start = 0
        best_len = float("inf")
        for i in range(len(t)):
            target[t[i]] = target.get(t[i], 0)+1
        need = len(target)
        for end in range(len(s)):
            window[s[end]] = window.get(s[end],0)+1
            if s[end] in target and window[s[end]] == target[s[end]]:
                have+=1
            while have == need:
                if best_len > end-start+1:
                    best_start = start
                    best_len = end-start+1
                window[s[start]] -=1
                if s[start] in target and window[s[start]] < target[s[start]]:
                    have-=1
                start+=1
        if best_len == float("inf"):
            return  ""
        return s[best_start:best_start + best_len]