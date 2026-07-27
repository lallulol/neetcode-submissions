class TimeMap:

    def __init__(self):
        self.MapTime = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.MapTime.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.MapTime:
            return ""
        values_list = self.MapTime[key]
        low = 0
        high = len(values_list)-1
        ans = ""
        while low <= high:
            mid = low + (high-low)//2
            if values_list[mid][1] <= timestamp:
                ans = values_list[mid][0]
                low = mid+1
            else:
                high=mid-1
        return ans


