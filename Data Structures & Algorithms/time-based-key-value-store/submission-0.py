class TimeMap:

    def __init__(self):
        self.data = {} # key, value [value, timestamp] pair

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        value = self.data.get(key, []) # get the key, if not return empty list

        l, r = 0, len(value) - 1
        while l <= r:
            m = (l + r) // 2
            if value[m][1] <= timestamp:
                result = value[m][0]
                l = m + 1
            else:
                r = m - 1

        return result