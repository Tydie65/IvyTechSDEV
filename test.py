import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [4, 5, 7, 9]
        result = sum(data)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()