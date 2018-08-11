import unittest
import summarizer as sm


class TestSummarizer(unittest.TestCase):
    def test_summary_written(self):
        # make sure summary is created
        with open("test.txt", "r") as test:
            test_string = test.read()
            test_summary = sm.summarize(test_string)
        self.assertTrue(test_summary)

    def test_length_summary(self):
        with open("test.txt", "r") as test:
            # make sure length is within acceptabele range of value
            test_string = test.read()
            test_summary = sm.summarize(test_string, value=0.2)

            length_string = len(test_string.split())
            length_summary = len(test_summary.split())
            self.assertTrue(length_summary -
                            (0.1 * length_summary) <= length_string * 0.2
                            <= length_summary + (0.1 * length_summary))
