# coding: utf-8

import unittest
from people_names import people_names

class ReutersTests(unittest.TestCase):
    def test_split_name_fml(self):
        names = people_names.split_name('', 'fml')
        self.assertEqual(names['first_name'], '')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], '')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], '')


        names = people_names.split_name('Ms. Jacqueline Williams-Roll', 'fml')
        self.assertEqual(names['first_name'], 'Jacqueline')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Williams-Roll')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Ms')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'jacqueline-williams-roll')


        names = people_names.split_name('Mr. Archbold van Beuren', 'fml')
        self.assertEqual(names['first_name'], 'Archbold')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'van Beuren')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'archbold-van-beuren')


        names = people_names.split_name('Jan van der Velden', 'fml')
        self.assertEqual(names['first_name'], 'Jan')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'van der Velden')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'jan-van-der-velden')


        names = people_names.split_name('Dr. Harry F. Hixson Jr.', 'fml')
        self.assertEqual(names['first_name'], 'Harry')
        self.assertEqual(names['middle_name'], 'F')
        self.assertEqual(names['last_name'], 'Hixson')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'harry-f-hixson')


        names = people_names.split_name('Marshall S. McCrea, III', 'fml')
        self.assertEqual(names['first_name'], 'Marshall')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'McCrea')
        self.assertEqual(names['suffix_name'], 'III')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'marshall-s-mccrea')


        names = people_names.split_name('James R. (Rick) Perry', 'fml')
        self.assertEqual(names['first_name'], 'James')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Perry')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], 'Rick')
        self.assertEqual(names['slug_name'], 'james-r-perry')



        names = people_names.split_name('Robert D. Cochran Esq.', 'fml')
        self.assertEqual(names['first_name'], 'Robert')
        self.assertEqual(names['middle_name'], 'D')
        self.assertEqual(names['last_name'], 'Cochran')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Esq')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'robert-d-cochran')


        names = people_names.split_name('Dr. Michael Severino, M.D.', 'fml')
        self.assertEqual(names['first_name'], 'Michael')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Severino')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'michael-severino')


        names = people_names.split_name('Ms. Diane de Saint Victor', 'fml')
        self.assertEqual(names['first_name'], 'Diane')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'de Saint Victor')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Ms')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'diane-de-saint-victor')


        names = people_names.split_name('Mr. Matthew S. Ramsey, J.D.', 'fml')
        self.assertEqual(names['first_name'], 'Matthew')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'Ramsey')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'matthew-s-ramsey')


        names = people_names.split_name('Mr. Samuel C. Scott, III.', 'fml')
        self.assertEqual(names['first_name'], 'Samuel')
        self.assertEqual(names['middle_name'], 'C')
        self.assertEqual(names['last_name'], 'Scott')
        self.assertEqual(names['suffix_name'], 'III')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'samuel-c-scott')


        names = people_names.split_name('Hon., Amb., Craig R. Stapleton', 'fml')
        self.assertEqual(names['first_name'], 'Craig')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Stapleton')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Hon')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'craig-r-stapleton')


        names = people_names.split_name('Lt. Gen.(Retd). Richard V. Reynolds', 'fml')
        self.assertEqual(names['first_name'], 'Richard')
        self.assertEqual(names['middle_name'], 'V')
        self.assertEqual(names['last_name'], 'Reynolds')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Lt')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'richard-v-reynolds')


        names = people_names.split_name('Mr. Keith E. St. Clair', 'fml')
        self.assertEqual(names['first_name'], 'Keith')
        self.assertEqual(names['middle_name'], 'E')
        self.assertEqual(names['last_name'], 'St Clair')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'keith-e-st-clair')


        names = people_names.split_name('Mr. Carlos W. del Solar Simpson', 'fml')
        self.assertEqual(names['first_name'], 'Carlos')
        self.assertEqual(names['middle_name'], 'W')
        self.assertEqual(names['last_name'], 'del Solar Simpson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'carlos-w-del-solar-simpson')


        names = people_names.split_name('Mr. Bernard de La Tour d\'Auvergne Lauraguais', 'fml')
        self.assertEqual(names['first_name'], 'Bernard')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'de La Tour d\'Auvergne Lauraguais')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'bernard-de-la-tour-dauvergne-lauraguais')


        names = people_names.split_name('Mr. Carlos Alberto da Veiga Sicupira', 'fml')
        self.assertEqual(names['first_name'], 'Carlos')
        self.assertEqual(names['middle_name'], 'Alberto')
        self.assertEqual(names['last_name'], 'da Veiga Sicupira')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'carlos-alberto-da-veiga-sicupira')


        names = people_names.split_name('Mr. Mauro di Carlo', 'fml')
        self.assertEqual(names['first_name'], 'Mauro')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'di Carlo')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'mauro-di-carlo')


        names = people_names.split_name('Mr. Warren East, CBE', 'fml')
        self.assertEqual(names['first_name'], 'Warren')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'East')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'warren-east')


        names = people_names.split_name('Gov. Hon. Tommy G. Thompson, J.D.', 'fml')
        self.assertEqual(names['first_name'], 'Tommy')
        self.assertEqual(names['middle_name'], 'G')
        self.assertEqual(names['last_name'], 'Thompson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gov')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'tommy-g-thompson')


        names = people_names.split_name('Fernando La Fuente Vila', 'fml')
        self.assertEqual(names['first_name'], 'Fernando')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'La Fuente Vila')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], '')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'fernando-la-fuente-vila')


        names = people_names.split_name('Mr. Eric G. Le Dain', 'fml')
        self.assertEqual(names['first_name'], 'Eric')
        self.assertEqual(names['middle_name'], 'G')
        self.assertEqual(names['last_name'], 'Le Dain')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'eric-g-le-dain')


        names = people_names.split_name('Prof. Lars G. Josefsson', 'fml')
        self.assertEqual(names['first_name'], 'Lars')
        self.assertEqual(names['middle_name'], 'G')
        self.assertEqual(names['last_name'], 'Josefsson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Prof')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'lars-g-josefsson')


        names = people_names.split_name('Mrs. Mary Callahan Erdoes', 'fml')
        self.assertEqual(names['first_name'], 'Mary')
        self.assertEqual(names['middle_name'], 'Callahan')
        self.assertEqual(names['last_name'], 'Erdoes')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mrs')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'mary-callahan-erdoes')


        names = people_names.split_name('Lieutenant General (Retired) George R. Christmas', 'fml')
        self.assertEqual(names['first_name'], 'George')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Christmas')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Lt')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'george-r-christmas')


        names = people_names.split_name('Mr. Timothy R. M. Main', 'fml')
        self.assertEqual(names['first_name'], 'Timothy')
        self.assertEqual(names['middle_name'], 'R M')
        self.assertEqual(names['last_name'], 'Main')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'timothy-r-m-main')


        names = people_names.split_name('Governor Brian D. Schweitzer', 'fml')
        self.assertEqual(names['first_name'], 'Brian')
        self.assertEqual(names['middle_name'], 'D')
        self.assertEqual(names['last_name'], 'Schweitzer')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gov')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'brian-d-schweitzer')


        names = people_names.split_name('Adm. (Retd.) Eric T. Olson', 'fml')
        self.assertEqual(names['first_name'], 'Eric')
        self.assertEqual(names['middle_name'], 'T')
        self.assertEqual(names['last_name'], 'Olson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Adm')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'eric-t-olson')


        names = people_names.split_name('Mr. Pedro Morazzani, CPA, C.V.A., C.F.E.', 'fml')
        self.assertEqual(names['first_name'], 'Pedro')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Morazzani')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'pedro-morazzani')


        names = people_names.split_name('Mr. Cesar A. Ortiz, CPA., J.D., Esq', 'fml')
        self.assertEqual(names['first_name'], 'Cesar')
        self.assertEqual(names['middle_name'], 'A')
        self.assertEqual(names['last_name'], 'Ortiz')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'cesar-a-ortiz')


        names = people_names.split_name('Mr. Philip S. "Scott" Moses', 'fml')
        self.assertEqual(names['first_name'], 'Philip')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'Moses')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], 'Scott')
        self.assertEqual(names['slug_name'], 'philip-s-moses')


        names = people_names.split_name('Mr. Christopher J. Reynolds, CGA', 'fml')
        self.assertEqual(names['first_name'], 'Christopher')
        self.assertEqual(names['middle_name'], 'J')
        self.assertEqual(names['last_name'], 'Reynolds')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'christopher-j-reynolds')


        names = people_names.split_name('Sen. William H. Frist M.D.', 'fml')
        self.assertEqual(names['first_name'], 'William')
        self.assertEqual(names['middle_name'], 'H')
        self.assertEqual(names['last_name'], 'Frist')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Sen')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'william-h-frist')


        names = people_names.split_name('Mr. John I. Von Lehman', 'fml')
        self.assertEqual(names['first_name'], 'John')
        self.assertEqual(names['middle_name'], 'I')
        self.assertEqual(names['last_name'], 'Von Lehman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'john-i-von-lehman')


        names = people_names.split_name('Mr. Sergio Traversa Pharm.D. MBA.', 'fml')
        self.assertEqual(names['first_name'], 'Sergio')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Traversa')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'sergio-traversa')


        names = people_names.split_name('Mr. Andrew ("Andy") Arno', 'fml')
        self.assertEqual(names['first_name'], 'Andrew')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Arno')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], 'Andy')
        self.assertEqual(names['slug_name'], 'andrew-arno')


        names = people_names.split_name('Mr. LI Xinzhou (Paul Li)', 'fml')
        self.assertEqual(names['first_name'], 'LI')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Xinzhou')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], 'Paul Li')
        self.assertEqual(names['slug_name'], 'li-xinzhou')


        names = people_names.split_name('Mr. Stephen T. Wills, MST, CPA', 'fml')
        self.assertEqual(names['first_name'], 'Stephen')
        self.assertEqual(names['middle_name'], 'T')
        self.assertEqual(names['last_name'], 'Wills')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'stephen-t-wills')


        names = people_names.split_name('Mr. Robert A. Dickinson, B.Sc., M.Sc.', 'fml')
        self.assertEqual(names['first_name'], 'Robert')
        self.assertEqual(names['middle_name'], 'A')
        self.assertEqual(names['last_name'], 'Dickinson')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'robert-a-dickinson')


        names = people_names.split_name('Mr. Gerald J. McConnell, QC', 'fml')
        self.assertEqual(names['first_name'], 'Gerald')
        self.assertEqual(names['middle_name'], 'J')
        self.assertEqual(names['last_name'], 'McConnell')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'gerald-j-mcconnell')


        names = people_names.split_name('Gen. Janet Carol Wolfenbarger, USAF, Retired', 'fml')
        self.assertEqual(names['first_name'], 'Janet')
        self.assertEqual(names['middle_name'], 'Carol')
        self.assertEqual(names['last_name'], 'Wolfenbarger')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'janet-carol-wolfenbarger')


        names = people_names.split_name('Gen.(Retd.) Ronald R. Fogleman', 'fml')
        self.assertEqual(names['first_name'], 'Ronald')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Fogleman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'ronald-r-fogleman')


        names = people_names.split_name('Gen.(Retd.) Peter Pace', 'fml')
        self.assertEqual(names['first_name'], 'Peter')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Pace')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'peter-pace')


        names = people_names.split_name('Gen. (Retd.) Peter Pace', 'fml')
        self.assertEqual(names['first_name'], 'Peter')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Pace')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'peter-pace')


        names = people_names.split_name('General Peter Pace, USMC (Retd.)', 'fml')
        self.assertEqual(names['first_name'], 'Peter')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Pace')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Gen')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'peter-pace')


        names = people_names.split_name('Mr. Trevor Thomas, LLB.', 'fml')
        self.assertEqual(names['first_name'], 'Trevor')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Thomas')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'trevor-thomas')


        names = people_names.split_name('Mr. David E. De Witt, B.Com., LLB.', 'fml')
        self.assertEqual(names['first_name'], 'David')
        self.assertEqual(names['middle_name'], 'E')
        self.assertEqual(names['last_name'], 'De Witt')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'david-e-de-witt')


        names = people_names.split_name('Mr. Ronald W. Thiessen, FCPA, FCA.', 'fml')
        self.assertEqual(names['first_name'], 'Ronald')
        self.assertEqual(names['middle_name'], 'W')
        self.assertEqual(names['last_name'], 'Thiessen')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'ronald-w-thiessen')


        names = people_names.split_name('Mr. Gordon B. Keep, B.Sc., MBA, P.Geo.', 'fml')
        self.assertEqual(names['first_name'], 'Gordon')
        self.assertEqual(names['middle_name'], 'B')
        self.assertEqual(names['last_name'], 'Keep')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'gordon-b-keep')


        names = people_names.split_name('Mr. Christian Milau, CPA, CA, CPA (Illinois)', 'fml')
        self.assertEqual(names['first_name'], 'Christian')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Milau')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'christian-milau')


        names = people_names.split_name('Mr. David Laing, BSc Mining Engineering', 'fml')
        self.assertEqual(names['first_name'], 'David')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Laing')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'david-laing')


        names = people_names.split_name('Dr. Daniel S. J. Muffoletto, N.D.', 'fml')
        self.assertEqual(names['first_name'], 'Daniel')
        self.assertEqual(names['middle_name'], 'S J')
        self.assertEqual(names['last_name'], 'Muffoletto')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'daniel-s-j-muffoletto')


        names = people_names.split_name('Comdr. Rigel D. Pirrone, USN', 'fml')
        self.assertEqual(names['first_name'], 'Rigel')
        self.assertEqual(names['middle_name'], 'D')
        self.assertEqual(names['last_name'], 'Pirrone')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Comdr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'rigel-d-pirrone')


        names = people_names.split_name('Mr. Donald W. Hedges , Esq.', 'fml')
        self.assertEqual(names['first_name'], 'Donald')
        self.assertEqual(names['middle_name'], 'W')
        self.assertEqual(names['last_name'], 'Hedges')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'donald-w-hedges')


        names = people_names.split_name('Ms. Susan Ludley, FCCA', 'fml')
        self.assertEqual(names['first_name'], 'Susan')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Ludley')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Ms')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'susan-ludley')


        names = people_names.split_name('Dr. William M. Harvey, B.A., Ph.D.', 'fml')
        self.assertEqual(names['first_name'], 'William')
        self.assertEqual(names['middle_name'], 'M')
        self.assertEqual(names['last_name'], 'Harvey')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'william-m-harvey')


        names = people_names.split_name('Mr. Ulrich E. Rath, B.Sc.(Hons), M.Sc.(Geol.)', 'fml')
        self.assertEqual(names['first_name'], 'Ulrich')
        self.assertEqual(names['middle_name'], 'E')
        self.assertEqual(names['last_name'], 'Rath')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'ulrich-e-rath')


        names = people_names.split_name('Ms. Rosalind Morrow, B.A., B.Ed.,A.R.C.T,LL.B.', 'fml')
        self.assertEqual(names['first_name'], 'Rosalind')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Morrow')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Ms')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'rosalind-morrow')


        names = people_names.split_name('Honorable Judge Arthur J. Gajarsa ', 'fml')
        self.assertEqual(names['first_name'], 'Arthur')
        self.assertEqual(names['middle_name'], 'J')
        self.assertEqual(names['last_name'], 'Gajarsa')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Hon')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'arthur-j-gajarsa')


        names = people_names.split_name('Mr. Russell E. Hallbauer, Prof. Eng.', 'fml')
        self.assertEqual(names['first_name'], 'Russell')
        self.assertEqual(names['middle_name'], 'E')
        self.assertEqual(names['last_name'], 'Hallbauer')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'russell-e-hallbauer')


        names = people_names.split_name('Mr. C. Thomas Ogryzlo, B.Mech., Eng., P.Eng', 'fml')
        self.assertEqual(names['first_name'], 'C')
        self.assertEqual(names['middle_name'], 'Thomas')
        self.assertEqual(names['last_name'], 'Ogryzlo')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'c-thomas-ogryzlo')


        names = people_names.split_name('Dr. Jerrold B. Grossman, D.P.S.', 'fml')
        self.assertEqual(names['first_name'], 'Jerrold')
        self.assertEqual(names['middle_name'], 'B')
        self.assertEqual(names['last_name'], 'Grossman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'jerrold-b-grossman')


        names = people_names.split_name('Dr. William W. R. Elder, OBE', 'fml')
        self.assertEqual(names['first_name'], 'William')
        self.assertEqual(names['middle_name'], 'W R')
        self.assertEqual(names['last_name'], 'Elder')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'william-w-r-elder')


        names = people_names.split_name('Dr. Lesley Russell Cooper, M.B.Ch.B.', 'fml')
        self.assertEqual(names['first_name'], 'Lesley')
        self.assertEqual(names['middle_name'], 'Russell')
        self.assertEqual(names['last_name'], 'Cooper')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'lesley-russell-cooper')


        names = people_names.split_name('Mr. Timothy W. Wilhite, Esquire', 'fml')
        self.assertEqual(names['first_name'], 'Timothy')
        self.assertEqual(names['middle_name'], 'W')
        self.assertEqual(names['last_name'], 'Wilhite')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'timothy-w-wilhite')


        names = people_names.split_name('Dr. Jeffrey W. Sherman, M.D., FACP.', 'fml')
        self.assertEqual(names['first_name'], 'Jeffrey')
        self.assertEqual(names['middle_name'], 'W')
        self.assertEqual(names['last_name'], 'Sherman')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'jeffrey-w-sherman')


        names = people_names.split_name('Mr. Vincent Della Volpe', 'fml')
        self.assertEqual(names['first_name'], 'Vincent')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Della Volpe')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'vincent-della-volpe')


        names = people_names.split_name('Justice Randall T. Shepard', 'fml')
        self.assertEqual(names['first_name'], 'Randall')
        self.assertEqual(names['middle_name'], 'T')
        self.assertEqual(names['last_name'], 'Shepard')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Justice')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'randall-t-shepard')


        names = people_names.split_name('Lt. Col. Katherine E. White', 'fml')
        self.assertEqual(names['first_name'], 'Katherine')
        self.assertEqual(names['middle_name'], 'E')
        self.assertEqual(names['last_name'], 'White')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Lt')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'katherine-e-white')


        names = people_names.split_name('Dr. Peter A. Demopulos, M.D., FACC, FSCAI', 'fml')
        self.assertEqual(names['first_name'], 'Peter')
        self.assertEqual(names['middle_name'], 'A')
        self.assertEqual(names['last_name'], 'Demopulos')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'peter-a-demopulos')


        names = people_names.split_name('Dr. Stephen G. Dilly, M.B.B.S., Ph.D.', 'fml')
        self.assertEqual(names['first_name'], 'Stephen')
        self.assertEqual(names['middle_name'], 'G')
        self.assertEqual(names['last_name'], 'Dilly')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'stephen-g-dilly')


        names = people_names.split_name('Adv. Ayelet Horn', 'fml')
        self.assertEqual(names['first_name'], 'Ayelet')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Horn')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Adv')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'ayelet-horn')


        names = people_names.split_name('Mr. Donald J. Carty LL.D.', 'fml')
        self.assertEqual(names['first_name'], 'Donald')
        self.assertEqual(names['middle_name'], 'J')
        self.assertEqual(names['last_name'], 'Carty')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'donald-j-carty')


        names = people_names.split_name('Shri. Nabankur Gupta', 'fml')
        self.assertEqual(names['first_name'], 'Nabankur')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Gupta')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Shri')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'nabankur-gupta')


        names = people_names.split_name('Mr. Errol R. Halperin, J.D., L.L.M.', 'fml')
        self.assertEqual(names['first_name'], 'Errol')
        self.assertEqual(names['middle_name'], 'R')
        self.assertEqual(names['last_name'], 'Halperin')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'errol-r-halperin')


        names = people_names.split_name('Mr.Yong Chen', 'fml')
        self.assertEqual(names['first_name'], 'Yong')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Chen')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'yong-chen')


        names = people_names.split_name('Mr. Fernando d\'Ornellas (Silva)', 'fml')
        self.assertEqual(names['first_name'], 'Fernando')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'd\'Ornellas')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], 'Silva')
        self.assertEqual(names['slug_name'], 'fernando-dornellas')


        names = people_names.split_name('Adm., Dr. (Retd.), Richard H. Carmona, M.D., M.P.H., FACS', 'fml')
        self.assertEqual(names['first_name'], 'Richard')
        self.assertEqual(names['middle_name'], 'H')
        self.assertEqual(names['last_name'], 'Carmona')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Adm')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'richard-h-carmona')


        names = people_names.split_name('Mr. Rupert Vessey, MA, BM BCh, FRCP.', 'fml')
        self.assertEqual(names['first_name'], 'Rupert')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Vessey')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'rupert-vessey')


        names = people_names.split_name('Prof. Hans-Peter Hartung MD, PhD, FRCP.', 'fml')
        self.assertEqual(names['first_name'], 'Hans-Peter')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Hartung')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Prof')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'hans-peter-hartung')


        names = people_names.split_name('Mr. Kevin Systrom,is', 'fml')
        self.assertEqual(names['first_name'], 'Kevin')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Systrom')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'kevin-systrom')


        names = people_names.split_name('Mr. Ernst J. Bartschi, LIC.OEC.HSG', 'fml')
        self.assertEqual(names['first_name'], 'Ernst')
        self.assertEqual(names['middle_name'], 'J')
        self.assertEqual(names['last_name'], 'Bartschi')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'ernst-j-bartschi')


        names = people_names.split_name('Mr. Patrick J. Kennedy, MBS, BComm.', 'fml')
        self.assertEqual(names['first_name'], 'Patrick')
        self.assertEqual(names['middle_name'], 'J')
        self.assertEqual(names['last_name'], 'Kennedy')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Mr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'patrick-j-kennedy')


        names = people_names.split_name('Dr. James S. Shannon, M.D., MRCP (UK)', 'fml')
        self.assertEqual(names['first_name'], 'James')
        self.assertEqual(names['middle_name'], 'S')
        self.assertEqual(names['last_name'], 'Shannon')
        self.assertEqual(names['suffix_name'], '')
        self.assertEqual(names['nominal_name'], 'Dr')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'james-s-shannon')


        names = people_names.split_name('Major General Josue Robles Jr., USA (Retired)', 'fml')
        self.assertEqual(names['first_name'], 'Josue')
        self.assertEqual(names['middle_name'], '')
        self.assertEqual(names['last_name'], 'Robles')
        self.assertEqual(names['suffix_name'], 'Jr')
        self.assertEqual(names['nominal_name'], 'Maj')
        self.assertEqual(names['nickname'], '')
        self.assertEqual(names['slug_name'], 'josue-robles')


# python -m unittest discover -s tests -p "*_tests.py"
