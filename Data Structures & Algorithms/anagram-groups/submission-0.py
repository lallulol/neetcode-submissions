class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_dict = defaultdict(list)
        for word in strs:
            alpha_list = [0]*26
            for char in word:
                alpha_list[ord(char) - ord('a')] += 1
            main_dict[tuple(alpha_list)].append(word)
        
        return list(main_dict.values())