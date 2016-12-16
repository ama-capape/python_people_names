# coding: utf-8

import unittest
from people_names import people_names

class UtilsTests(unittest.TestCase):
    def test_split_name_fml(self):
        names = people_names.split_name('Federico F. Peña', 'fml')
        self.assertEqual(names['first_name'], 'Federico')
        self.assertEqual(names['middle_name'], 'F')
        self.assertEqual(names['last_name'], 'Pena')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'federico-f-pena')


        names = people_names.split_name('Arthur D. Collins, Jr.*', 'fml')
        self.assertEqual(names['first_name'], 'Arthur')
        self.assertEqual(names['middle_name'], 'D')
        self.assertEqual(names['last_name'], 'Collins')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'arthur-d-collins')

# python -m unittest discover -s tests -p "*_tests.py"
