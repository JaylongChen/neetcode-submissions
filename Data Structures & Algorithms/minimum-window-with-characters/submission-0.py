class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        # build frequency for t string characters
        countT = {}
        window = {}
        result = [-1, -1]
        resultLen = float("infinity")

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        l, r = 0, 0
        # have: # of matching
        # need: # of needed
        have, need = 0, len(countT)
        
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            
            # check if current char is in T
            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1
            
            # when matched
            while have == need:
                # update current result length
                if r - l + 1 < resultLen:
                    result = s[l : r + 1]
                    resultLen = r - l + 1

                if s[l] in countT and window[s[l]] == countT[s[l]]:
                    have -= 1

                window[s[l]] -= 1
                l += 1

        if resultLen != float("infinity"):
            return result
        else:
            return "" 
                

            

        
