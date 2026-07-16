class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0)+1

        s_list = sorted(dict.items(), key=lambda item: item[1], reverse=True)
        top_keys = [item[0] for item in s_list[:k]]

        return(top_keys)
