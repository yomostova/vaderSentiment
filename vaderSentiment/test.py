import unittest

from vaderSentiment import SentimentIntensityAnalyzer


class MyTestCase(unittest.TestCase):
    def test_phrase_(self):
        analyzer = SentimentIntensityAnalyzer()
        sentence = "I see now cashtag burn."
        result = analyzer.polarity_scores(sentence)
        self.assertEqual(str(result), "{'neg': 0.0, 'neu': 0.588, 'pos': 0.412, 'compound': 0.4215}")  # add assertion here


if __name__ == '__main__':
    unittest.main()
