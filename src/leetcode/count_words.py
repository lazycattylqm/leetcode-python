from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        res = 0
        for w in count1:
            if count1[w] == 1 and count2[w] == 1:
                res += 1
        return res

