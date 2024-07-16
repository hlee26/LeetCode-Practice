class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolarray = []

        for candy in candies:
            if candy + extraCandies >= max(candies):
                boolarray.append(True)
            else:
                boolarray.append(False)

        return(boolarray)