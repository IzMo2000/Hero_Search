import unittest
from search_feature import get_result_value


class searchFeature(unittest.TestCase):
    def test_getResultValue(self):
        self.assertEqual(get_result_value("Batman"), None)


if __name__ == '__main__':
    unittest.main()
