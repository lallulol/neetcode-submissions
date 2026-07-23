class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0  
        counts = {}
        right_counts = {}

        for i in range(len(s1)):
            counts[s1[i]] = counts.get(s1[i], 0)+1
    
        for end in range(len(s2)):
            right_counts[s2[end]] = right_counts.get(s2[end],0)+1
            if (end-start+1)==len(s1):
                if counts == right_counts:
                    return True
                right_counts[s2[start]]-=1
                if right_counts[s2[start]] == 0:
                    del right_counts[s2[start]]
                start+=1
        return False
