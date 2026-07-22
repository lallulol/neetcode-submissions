class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        best = 0
        max_count = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(count[s[end]],max_count)
            while (end - start + 1) - max_count > k:
                count[s[start]] -= 1
                start += 1
            best = max(best, end - start + 1)
        return best