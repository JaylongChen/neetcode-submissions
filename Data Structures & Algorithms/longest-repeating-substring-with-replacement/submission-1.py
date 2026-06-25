class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxFreq = 0
        l = 0
        result = 0

        for r in range(len(s)):
            #building the sliding window freq dict
            # increase the count by 1, and initialize to 0 when not in dict
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            # shift left pointer when sliding window is invalid
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)

        return result
        
