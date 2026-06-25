class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            arr = [0] * 26 # [0,0,0,0,0,0,0 etc]
            for char in string:
                arr[ord(char) - ord('a')] += 1
            result[tuple(arr)].append(string)
        
        return list(result.values())

        