class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encode a list of strings to a single string"""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s  # longueur + '#' + mot
        return res

    def decode(self, s: str) -> List[str]:
        """Decode a single string to a list of strings"""
        res = []
        i = 0
        while i < len(s):
            # lire la longueur
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            # lire le mot
            word = s[j+1:j+1+length]
            res.append(word)
            
            # avancer l'index
            i = j + 1 + length
        return res