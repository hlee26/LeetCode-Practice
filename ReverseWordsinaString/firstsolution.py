class Solution:
    def reverseWords(self, s: str) -> str:
        new = list(s.split())
        i = 0
        l = len(new)-1
        while i<l:
            if ( new[i] or new[l] ) != '':
                new[i], new[l] = new[l].strip(), new[i].strip()
            i += 1
            l -= 1
        return ' '.join(new)