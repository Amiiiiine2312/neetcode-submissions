class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s_copie = ""
        for i in range (len(s)):
            if s[i] in alph:
                s_copie = s_copie + s[i]
        i=0
        j=len(s_copie)-1
        s_copie = s_copie.lower()
        while (i < j):
            if s_copie[i] != s_copie[j]:
                return False
            else:
                i+=1
                j-=1
        return True