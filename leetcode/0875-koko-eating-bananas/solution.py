from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # predicate: can we finish in <= h hours at speed k?
        def can(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k  # integer ceil
            return hours <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid  # mid works → try smaller
            else:
                lo = mid + 1  # too slow → need larger
        return lo
