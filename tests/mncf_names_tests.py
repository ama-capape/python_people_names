# coding: utf-8

import unittest
from people_names import people_names

class MncfTests(unittest.TestCase):
    def test_split_name_fml(self):
        names = people_names.split_name('Torkelson, Paul, M', 'lfm')
        self.assertEqual(names['first_name'], 'Paul')
        self.assertEqual(names['middle_name'], 'M')
        self.assertEqual(names['last_name'], 'Torkelson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'paul-m-torkelson')

        names = people_names.split_name('Vogel, Robert (Bob)', 'lfm')
        self.assertEqual(names['first_name'], 'Robert')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Vogel')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], 'Bob')
        self.assertEqual(names['slug_name'], 'robert-vogel')

        names = people_names.split_name('Zick, Robert (Bob), S', 'lfm')
        self.assertEqual(names['first_name'], 'Robert')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'Zick')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], 'Bob')
        self.assertEqual(names['slug_name'], 'robert-s-zick')

        names = people_names.split_name('Timmerman Michael', 'lfm', True)
        self.assertEqual(names['first_name'], 'Michael')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Timmerman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'michael-timmerman')

# python -m unittest discover -s tests -p "*_tests.py"
