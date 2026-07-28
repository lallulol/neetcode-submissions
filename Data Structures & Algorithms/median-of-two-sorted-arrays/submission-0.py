class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numss = sorted(nums1+nums2)
        total_len = len(numss)
        if total_len %2 == 0:
            first = total_len//2
            second = first-1
            save1 = numss[first]
            save2 = numss[second]
            return (save1+save2)/2
        else:
            first = total_len//2
            return numss[first]/1