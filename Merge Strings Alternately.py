class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        new = []
        i = 0

        while(i < len1 or i < len2):

            if(i < len1):
                new.append(word1[i])

            if(i < len2):
                new.append(word2[i])

            i = i + 1

        return ''.join(new)