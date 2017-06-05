import unittest
from people_names import people_names

class UtilsTests(unittest.TestCase):
    def test_add_name_parts_to_dict(self):
        obj = {'job': 'auror'}
        name_parts = {
            'first_name': 'harry',
            'middle_name': 'james',
            'last_name': 'potter',
            'suffix_name': '',
            'nominal_name': 'Sir',
            'nickname': 'the choosen one',
            'slug_name': 'harry-james-potter'
        }
        people_names.add_name_parts_to_dict(obj, name_parts)
        self.assertEqual(obj['first_name'], 'harry')
        self.assertEqual(obj['middle_name'], 'james')
        self.assertEqual(obj['last_name'], 'potter')
        self.assertEqual(obj['suffix_name'], '')
        self.assertEqual(obj['nominal_name'], 'Sir')
        self.assertEqual(obj['nickname'], 'the choosen one')
        self.assertEqual(obj['slug_name'], 'harry-james-potter')

    def test_invalid_name_format(self):
        names = people_names.split_name('potter, harry', 'lmf')
        self.assertEqual(names['err'], 'invalid name format...')
# python -m unittest discover -s tests -p "*_tests.py"
