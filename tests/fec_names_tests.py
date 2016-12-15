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

        # names = people_names.split_name('MORRIS, III, WILLIAM N.', 'lfm')
        # self.assertEqual(names['first_name'], 'William')
        # self.assertEqual(names['middle_name'], 'N')
        # self.assertEqual(names['last_name'], 'Morris')
        # self.assertEqual(names['suffix_name'], 'III')
        # self.assertEqual(names['nominal_name'], '')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], 'william-n-morris')
        #
        # names = people_names.split_name('SKINNER, JR', 'lfm')
        # self.assertEqual(names['first_name'], '')
        # self.assertEqual(names['middle_name'], '')
        # self.assertEqual(names['last_name'], 'Skinner')
        # self.assertEqual(names['suffix_name'], 'Jr')
        # self.assertEqual(names['nominal_name'], '')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], 'skinner')










        # names = people_names.split_name('ABDULHAMID, AMMAR', 'lfm')
        # self.assertEqual(names['first_name'], 'Ammar')
        # self.assertEqual(names['middle_name'], '')
        # self.assertEqual(names['last_name'], 'Abdulhamid')
        # self.assertEqual(names['suffix_name'], '')
        # self.assertEqual(names['nominal_name'], '')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('ABBOTT, GIFFORD WHEELER JR', 'lfm')
        # self.assertEqual(names['first_name'], 'Gifford')
        # self.assertEqual(names['middle_name'], 'Wheeler')
        # self.assertEqual(names['last_name'], 'Abbott')
        # self.assertEqual(names['suffix_name'], 'Jr')
        # self.assertEqual(names['nominal_name'], '')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('ABRAMS, MARCIA KAREN DR PHD', 'lfm')
        # self.assertEqual(names['first_name'], 'Marcia')
        # self.assertEqual(names['middle_name'], 'Karen')
        # self.assertEqual(names['last_name'], 'Abrams')
        # self.assertEqual(names['suffix_name'], '')
        # self.assertEqual(names['nominal_name'], 'Dr')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('ABRAHAM, RALPH LEE DR. JR', 'lfm')
        # self.assertEqual(names['first_name'], 'Ralph')
        # self.assertEqual(names['middle_name'], 'Lee')
        # self.assertEqual(names['last_name'], 'Abraham')
        # self.assertEqual(names['suffix_name'], 'Jr')
        # self.assertEqual(names['nominal_name'], 'Dr')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('ALARCON, RICHARD ANTHONY MR.', 'lfm')
        # self.assertEqual(names['first_name'], 'Richard')
        # self.assertEqual(names['middle_name'], 'Anthony')
        # self.assertEqual(names['last_name'], 'Alarcon')
        # self.assertEqual(names['suffix_name'], '')
        # self.assertEqual(names['nominal_name'], 'Mr')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('ANNA, SANTA MR. THE III', 'lfm')
        # self.assertEqual(names['first_name'], 'Santa')
        # self.assertEqual(names['middle_name'], '')
        # self.assertEqual(names['last_name'], 'Anna')
        # self.assertEqual(names['suffix_name'], 'III')
        # self.assertEqual(names['nominal_name'], 'Mr')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('ANTLEY, RAY MILLS JR MD', 'lfm')
        # self.assertEqual(names['first_name'], 'Ray')
        # self.assertEqual(names['middle_name'], 'Mills')
        # self.assertEqual(names['last_name'], 'Antley')
        # self.assertEqual(names['suffix_name'], 'Jr')
        # self.assertEqual(names['nominal_name'], 'MD')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('smith, JANE cpa', 'lfm')
        # self.assertEqual(names['first_name'], 'Jane')
        # self.assertEqual(names['middle_name'], '')
        # self.assertEqual(names['last_name'], 'Smith')
        # self.assertEqual(names['suffix_name'], '')
        # self.assertEqual(names['nominal_name'], 'CPA')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('BONIFICIA, ANTHONY A JR', 'lfm')
        # self.assertEqual(names['first_name'], 'Anthony')
        # self.assertEqual(names['middle_name'], 'A')
        # self.assertEqual(names['last_name'], 'Bonificia')
        # self.assertEqual(names['suffix_name'], 'Jr')
        # self.assertEqual(names['nominal_name'], '')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('VON ADAMS III, PHILIP MONROE', 'lfm')
        # self.assertEqual(names['first_name'], 'Philip')
        # self.assertEqual(names['middle_name'], 'Monroe')
        # self.assertEqual(names['last_name'], 'Von Adams')
        # self.assertEqual(names['suffix_name'], 'III')
        # self.assertEqual(names['nominal_name'], '')
        # self.assertEqual(names['nickname'], '')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('BRASS JR, HERMAN (GEORGE)', 'lfm')
        # self.assertEqual(names['first_name'], 'Herman')
        # self.assertEqual(names['middle_name'], '')
        # self.assertEqual(names['last_name'], 'Brass')
        # self.assertEqual(names['suffix_name'], 'Jr')
        # self.assertEqual(names['nominal_name'], '')
        # self.assertEqual(names['nickname'], 'George')
        # self.assertEqual(names['slug_name'], '')
        #
        # names = people_names.split_name('PERRY, JAMES R (RICK)', 'lfm')
        # self.assertEqual(names['first_name'], 'James')
        # self.assertEqual(names['middle_name'], 'R')
        # self.assertEqual(names['last_name'], 'Perry')
        # self.assertEqual(names['suffix_name'], '')
        # self.assertEqual(names['nominal_name'], '')
        # self.assertEqual(names['nickname'], 'Rick')
        # self.assertEqual(names['slug_name'], '')



# python -m unittest discover -s tests -p "*_tests.py"
