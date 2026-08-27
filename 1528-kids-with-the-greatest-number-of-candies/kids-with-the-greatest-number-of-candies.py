class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)

        return [candy + extraCandies >= maximum for candy in candies]