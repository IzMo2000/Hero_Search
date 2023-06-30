import unittest
import os
from search_feature import get_result_value, print_hero_data, default_display
from search_feature import check_input_string, implement_table, hero_stat
from search_feature import display_hero_data, clear_data, display_data

dummy_hero = {
    'name': 'The Tester',
    'description': 'The ultimate tester of all code!',
    'comics': {'available': 300},
    'series': {'available': 500},
    'stories': {'available': 200},
    'events': {'available': 100},
}


dummy_stats = {
            'name': 'The Tester',
            'comics': 300,
            'series': 500,
            'stories': 200,
            'events': 100
        }


class searchFeature(unittest.TestCase):
    def test_getResultValue(self):
        self.assertEqual(get_result_value("Batman"), None)
        self.assertIsInstance(get_result_value("Thor"), dict)

    def test_printHeroData(self):
        self.assertTrue(print_hero_data(dummy_hero))
        self.assertFalse(print_hero_data({}))

    def test_heroStat(self):
        self.assertEqual(hero_stat(dummy_hero), dummy_stats)

    def test_checkInputString(self):
        self.assertEqual(check_input_string("The Tester"),
                         [True, "The Tester"])
        self.assertEqual(check_input_string(""), [False, ""])

    def test_implementTable(self):
        self.assertTrue(implement_table(dummy_stats))
        clear_data()

    def test_displayHeroData(self):
        implement_table(dummy_stats)
        self.assertFalse(display_hero_data("The Tester").empty)
        self.assertEqual(display_hero_data("Dummy Name"),
                         "No data found for Dummy Name.")
        clear_data()

    def test_clearData(self):
        implement_table(dummy_stats)
        self.assertEqual(clear_data(),
                         "History deleted successfully.  You are safe :) ")
        os.remove('hero_data.db')
        error_msg, error_dummy = clear_data()
        self.assertEqual(error_msg, "Error occurred while deleting data:")

    def test_displayData(self):
        implement_table(dummy_stats)
        self.assertFalse(display_data().empty)
        clear_data()
        self.assertEqual(display_data(), "No data available.")

    def test_defaultDisplay(self):
        implement_table(dummy_stats)
        self.assertFalse(default_display().empty)
        clear_data()
        self.assertEqual(default_display(), "No data available.")


if __name__ == '__main__':
    unittest.main()
