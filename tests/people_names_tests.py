import unittest
from people_names import people_names

class UtilsTests(unittest.TestCase):
    def test_split_name_fml(self):
        names = people_names.split_name('', 'fml')
        self.assertEqual(names['first_name'], '')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], '')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Jacqueline Williams-Roll', 'fml')
        self.assertEqual(names['first_name'], 'Jacqueline')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Williams-Roll')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Archbold van Beuren', 'fml')
        self.assertEqual(names['first_name'], 'Archbold')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Van Beuren')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Jan van der Velden', 'fml')
        self.assertEqual(names['first_name'], 'Jan')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Van Der Velden')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Carl-Henric Svanberg', 'fml')
        self.assertEqual(names['first_name'], 'Carl-Henric')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Svanberg')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Harry F. Hixson Jr.', 'fml')
        self.assertEqual(names['first_name'], 'Harry')
        self.assertEqual(names['middle_name'], 'F.')
        self.assertEqual(names['last_name'], 'Hixson')
        self.assertEqual(names['suffix_name'], 'Jr.')

    def test_split_name_lmf(self):
        names = people_names.split_name('', 'lfm')
        self.assertEqual(names['first_name'], '')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], '')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('Davis, Alicia Boler', 'lmf')
        self.assertEqual(names['first_name'], 'Alicia')
        self.assertEqual(names['middle_name'], 'Boler')
        self.assertEqual(names['last_name'], 'Davis')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('ABDULHAMID, AMMAR', 'lmf')
        self.assertEqual(names['first_name'], 'Ammar')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Abdulhamid')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('ABBOTT, GIFFORD WHEELER JR', 'lmf')
        self.assertEqual(names['first_name'], 'Gifford')
        self.assertEqual(names['middle_name'], 'Wheeler')
        self.assertEqual(names['last_name'], 'Abbott')
        self.assertEqual(names['suffix_name'], 'Jr.')

        names = people_names.split_name('ABRAMS, MARCIA KAREN DR PHD', 'lmf')
        self.assertEqual(names['first_name'], 'Marcia')
        self.assertEqual(names['middle_name'], 'Karen')
        self.assertEqual(names['last_name'], 'Abrams')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('ABRAHAM, RALPH LEE DR. JR', 'lmf')
        self.assertEqual(names['first_name'], 'Ralph')
        self.assertEqual(names['middle_name'], 'Lee')
        self.assertEqual(names['last_name'], 'Abraham')
        self.assertEqual(names['suffix_name'], 'Jr.')

        names = people_names.split_name('ALARCON, RICHARD ANTHONY MR.', 'lmf')
        self.assertEqual(names['first_name'], 'Richard')
        self.assertEqual(names['middle_name'], 'Anthony')
        self.assertEqual(names['last_name'], 'Alarcon')
        self.assertEqual(names['suffix_name'], '')

        names = people_names.split_name('ANNA, SANTA MR. THE III', 'lmf')
        self.assertEqual(names['first_name'], 'Santa')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Anna')
        self.assertEqual(names['suffix_name'], 'III')

        names = people_names.split_name('ANTLEY, RAY MILLS JR MD', 'lmf')
        self.assertEqual(names['first_name'], 'Ray')
        self.assertEqual(names['middle_name'], 'Mills')
        self.assertEqual(names['last_name'], 'Antley')
        self.assertEqual(names['suffix_name'], 'Jr.')

        names = people_names.split_name('BONIFICIA, ANTHONY A JR', 'lmf')
        self.assertEqual(names['first_name'], 'Anthony')
        self.assertEqual(names['middle_name'], 'A')
        self.assertEqual(names['last_name'], 'Bonificia')
        self.assertEqual(names['suffix_name'], 'Jr.')

        names = people_names.split_name('VON ADAMS III, PHILIP MONROE', 'lmf')
        self.assertEqual(names['first_name'], 'Philip')
        self.assertEqual(names['middle_name'], 'Monroe')
        self.assertEqual(names['last_name'], 'Von Adams')
        self.assertEqual(names['suffix_name'], 'III')

        names = people_names.split_name('BRASS JR, HERMAN (GEORGE)', 'lmf')
        self.assertEqual(names['first_name'], 'Herman')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Brass')
        self.assertEqual(names['suffix_name'], 'Jr.')



# python -m unittest discover -s tests -p "*_tests.py"
