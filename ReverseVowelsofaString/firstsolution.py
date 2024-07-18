class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        i = 0
        l = len(s)-1
        out = list(s)
        while i<l:
            if out[i] in vowels and out[l] in vowels:
                out[i],out[l] = out[l],out[i]
                i+=1
                l-=1
            if out[l] not in vowels:
                l-=1
            if out[i] not in vowels:
                i+=1

        return ''.join(out)