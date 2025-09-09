import bisect
from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    # tails[k] = min possible tail of an inc subsequence of length k+1
    tails: List[int] = []

    for x in nums:
        # find the leftmost i where tails[i] >= x
        i = bisect.bisect_left(tails, x)  # leftmost index where tails[i] >= x

        # if i == len(tails): append x
        if i == len(tails):
            tails.append(x)
        # else: replace tails[i] with x
        else:
            tails[i] = x

    # return the length of tails
    return len(tails)
