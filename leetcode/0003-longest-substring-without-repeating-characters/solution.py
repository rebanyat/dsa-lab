from typing import Dict


def lengthOfLongestSubstring(s: str) -> int:
    last: Dict[str, int] = {}
    L = 0
    best = 0
    for R, ch in enumerate(s):
        if ch in last and last[ch] >= L:
            L = last[ch] + 1
        best = max(best, R - L + 1)
        last[ch] = R
    return best
