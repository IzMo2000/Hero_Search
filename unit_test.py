import unittest
from search_feature import get_result_value, print_hero_data, hero_stat
from search_feature import validate_name

dummy_hero = {
    'name':'The Tester',
    'description':'The ultimate tester of all code!',
    'comics':{'available': 300},
    'series':{'available': 500},
    'stories':{'available': 200},
    'events':{'available': 100},
}


class searchFeature(unittest.TestCase):
    def test_getResultValue(self):
        self.assertEqual(get_result_value("Batman"), None)
        self.assertIsInstance(get_result_value("Thor"), dict)
    
    def test_printHeroData(self):
        self.assertTrue(print_hero_data(dummy_hero))
        self.assertFalse(print_hero_data({}))
    
    def test_heroStat(self):
        dummy_stats = {
            'name': 'The Tester',
            'comics': 300,
            'series': 500,
            'stories': 200,
            'events': 100
        }

        self.assertEqual(hero_stat(dummy_hero), dummy_stats)
    
    def test_validateName(self):
        self.assertEqual(validate_name("The Tester"), [True, "The Tester"])
        self.assertEqual(validate_name(""), [False, ""])


if __name__ == '__main__':
    unittest.main()
