class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        inGroup={}
        for i in range(len(strs)):
            codeI = "".join(sorted(strs[i]))
            if codeI not in inGroup :
                anagI = [strs[i]]
                inGroup[codeI] = anagI
            else : 
                inGroup[codeI].append(strs[i])
        return list(inGroup.values())


            