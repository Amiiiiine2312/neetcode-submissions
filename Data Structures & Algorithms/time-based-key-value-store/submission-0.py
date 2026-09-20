from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        items = self.map[key]
        i = bisect.bisect_right(items, (timestamp, chr(127))) 
        if i == 0:
            return ""
        return items[i-1][1]
