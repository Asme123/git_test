import unittest


def concatenate(a, b):
    return a + b


class TestConcatenate(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(concatenate("hello", "world"), "helloworld")
        self.assertEqual(concatenate("foo", " bar"), "foo bar")


if __name__ == "__main__":
    unittest.main()
