from unittest import TestCase
from src.leetcode.count_words import Solution

class TestSolution(TestCase):
    def test_count_words(self):
        solution = Solution()
        words = solution.countWords(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"])
        assert words==2
