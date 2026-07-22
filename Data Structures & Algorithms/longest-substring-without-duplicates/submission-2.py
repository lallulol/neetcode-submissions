class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_count = 0
        vocab = {}
        start = 0

        for i in range(len(s)):
            if s[i] in vocab and vocab[s[i]] >= start:
                start = vocab[s[i]] + 1

            vocab[s[i]] = i
            best_count = max(best_count, i - start + 1)

        return best_count