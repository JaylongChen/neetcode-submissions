class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for char in s:
            if char.isalnum():
                temp = temp + char
        print(temp)
        print(temp[::-1].lower())
        return temp.lower() == temp[::-1].lower()