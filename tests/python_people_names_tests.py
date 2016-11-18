import unittest
import python_people_names as people_names

class UtilsTests(unittest.TestCase):
    def test_split_name(self):
        names = people_names.split_name('')
        self.assertEqual(names['first_name'], '')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], '')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Jacqueline Williams-Roll')
        self.assertEqual(names['first_name'], 'Jacqueline')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Williams-Roll')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Alicia Boler Davis')
        self.assertEqual(names['first_name'], 'Alicia')
        self.assertEqual(names['middle_name'], 'Boler')
        self.assertEqual(names['last_name'], 'Davis')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('G. Zachary Gund')
        self.assertEqual(names['first_name'], 'G.')
        self.assertEqual(names['middle_name'], 'Zachary')
        self.assertEqual(names['last_name'], 'Gund')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Archbold van Beuren')
        self.assertEqual(names['first_name'], 'Archbold')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'van Beuren')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Jan van der Velden')
        self.assertEqual(names['first_name'], 'Jan')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'van der Velden')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Carl-Henric Svanberg')
        self.assertEqual(names['first_name'], 'Carl-Henric')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Svanberg')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Harry F. Hixson Jr.')
        self.assertEqual(names['first_name'], 'Harry')
        self.assertEqual(names['middle_name'], 'F.')
        self.assertEqual(names['last_name'], 'Hixson')
        self.assertEqual(names['suffix_name'], 'Jr.')

# python -m unittest discover -s tests -p "*_tests.py"
