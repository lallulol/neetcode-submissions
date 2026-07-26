class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = 0
        while low <= high:
            mid = low + (high-low)//2
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile/mid)
            if hours_needed <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans