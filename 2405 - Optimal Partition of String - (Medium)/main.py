class Solution:
    def partitionString(self, s: str) -> int:
        hashset = set()
        res = 1
        for c in s:
            if c in hashset:
                hashset = set()
                res+=1
            hashset.add(c)
        return res
