import unittest
from people_names import people_names

class UtilsTests(unittest.TestCase):
    def test_split_name_lfm(self):
        names = people_names.split_name('', 'lfm')
        self.assertEqual(names['first_name'], '')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], '')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], '')

        names = people_names.split_name('DNC SERVICES CORP.', 'lfm')
        self.assertIsNone(names)

        names = people_names.split_name('ROZIER, JAMES', 'lfm')
        self.assertEqual(names['first_name'], 'James')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Rozier')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'james-rozier')

        names = people_names.split_name('HOLLOMAN,MARILYN DAVIS', 'lfm')
        self.assertEqual(names['first_name'], 'Marilyn')
        self.assertEqual(names['middle_name'], 'Davis')
        self.assertEqual(names['last_name'], 'Holloman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'marilyn-davis-holloman')

# python -m unittest discover -s tests -p "*_tests.py"
