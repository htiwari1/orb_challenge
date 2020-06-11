import unittest
import problem_one
import problem_three

class TestStringMethods(unittest.TestCase):

    def test_problem_one(self):
        raw_names = [
        'SPV Inc., DBA: Super Company',
        'Michael Forsky LLC d.b.a F/B Burgers .',
        '*** Youthful You Aesthetics ***',
        'Aruna Indika (dba. NGXess)',
        'Diot SA, - D. B. A. *Diot-Technologies*',
        'PERFECT PRIVACY, LLC, d-b-a Perfection,',
        'PostgreSQL DB Analytics',
        '/JAYE INC/',
        ' ETABLISSEMENTS SCHEPENS /D.B.A./ ETS_SCHEPENS',
        'DUIKERSTRAINING OOSTENDE | D.B.A.: D.T.O. '
    ]

        cleaned_name_pairs = [
        ('SPV Inc', 'Super Company'),
        ('Michael Forsky LLC', 'F/B Burgers'),
        ('Youthful You Aesthetics', None),
        ('Aruna Indika', 'NGXess'),
        ('Diot SA', 'Diot-Technologies'),
        ('PERFECT PRIVACY, LLC', 'Perfection'),
        ('PostgreSQL DB Analytics', None),
        ('JAYE INC', None),
        ('ETABLISSEMENTS SCHEPENS', 'ETS SCHEPENS'),
        ('DUIKERSTRAINING OOSTENDE', 'D.T.O'),
    ]
        self.assertListEqual(problem_one.clean_names(raw_names), cleaned_name_pairs)

    def test_problem_three(self):

        expected_result = [{'office_name': 'Headquarters', 'office_link': 'http://www.dot.ca.gov', 'office_address': '1120 N Street', 'office_city': 'Sacramento', 'office_state': 'CA', 'office_zip': '95814', 'office_phone': '(916) 654-2852', 'mail_address': None, 'mail_pobox': 'P.O. Box 942873', 'mail_city': 'Sacramento', 'mail_state': 'CA', 'mail_zip': '94273-0001', 'mail_phone': None}, {'office_name': 'District 1', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-1', 'office_address': '1656 Union Street', 'office_city': 'Eureka', 'office_state': 'CA', 'office_zip': '95501', 'office_phone': '(707) 445-6600', 'mail_address': None, 'mail_pobox': 'P.O. Box 3700', 'mail_city': 'Eureka', 'mail_state': 'CA', 'mail_zip': '95502-3700', 'mail_phone': None}, {'office_name': 'District 2', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-2', 'office_address': '1657 Riverside Drive', 'office_city': 'Redding', 'office_state': 'CA', 'office_zip': '96001', 'office_phone': '(530) 225-3426', 'mail_address': '1657 Riverside Drive', 'mail_pobox': None, 'mail_city': 'Redding', 'mail_state': 'CA', 'mail_zip': '96001', 'mail_phone': None}, {'office_name': 'District 3', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-3', 'office_address': '703 B Street', 'office_city': 'Marysville', 'office_state': 'CA', 'office_zip': '95901', 'office_phone': '(530) 741-4572', 'mail_address': '703 B Street', 'mail_pobox': None, 'mail_city': 'Marysville', 'mail_state': 'CA', 'mail_zip': '95901', 'mail_phone': None}, {'office_name': 'District 4', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-4', 'office_address': '111 Grand Ave', 'office_city': 'Oakland', 'office_state': 'CA', 'office_zip': '94612', 'office_phone': '(510) 286-4444', 'mail_address': None, 'mail_pobox': 'P.O. Box 23660', 'mail_city': 'Oakland', 'mail_state': 'CA', 'mail_zip': '94623-0660', 'mail_phone': None}, {'office_name': 'District 5', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-5', 'office_address': '50 Higuera Street', 'office_city': 'San Luis Obispo', 'office_state': 'CA', 'office_zip': '93401-5415', 'office_phone': '(805) 549-3111', 'mail_address': '50 Higuera Street', 'mail_pobox': None, 'mail_city': 'San Luis Obispo', 'mail_state': 'CA', 'mail_zip': '93401-5415', 'mail_phone': None}, {'office_name': 'District 6', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-6', 'office_address': '1352 W. Olive Avenue', 'office_city': 'Fresno', 'office_state': 'CA', 'office_zip': '93728', 'office_phone': '(559) 444-2518', 'mail_address': None, 'mail_pobox': 'P.O. Box 12616', 'mail_city': 'Fresno', 'mail_state': 'CA', 'mail_zip': '93778-2616', 'mail_phone': None}, {'office_name': 'District 7', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-7', 'office_address': '100 South Main Street', 'office_city': 'Los Angeles', 'office_state': 'CA', 'office_zip': '90012', 'office_phone': '(213) 897-3656', 'mail_address': '100 South Main Street', 'mail_pobox': None, 'mail_city': 'Los Angeles', 'mail_state': 'CA', 'mail_zip': '90012', 'mail_phone': None}, {'office_name': 'District 8', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-8', 'office_address': '464 W. 4th Street', 'office_city': 'San Bernardino', 'office_state': 'CA', 'office_zip': '92401', 'office_phone': '(909) 383-4631', 'mail_address': '464 W. 4th Street', 'mail_pobox': None, 'mail_city': 'San Bernardino', 'mail_state': 'CA', 'mail_zip': '92401', 'mail_phone': None}, {'office_name': 'District 9', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-9', 'office_address': '500 South Main Street', 'office_city': 'Bishop', 'office_state': 'CA', 'office_zip': '93514', 'office_phone': '(760) 872-0601', 'mail_address': '500 South Main Street', 'mail_pobox': None, 'mail_city': 'Bishop', 'mail_state': 'CA', 'mail_zip': '93514', 'mail_phone': None}, {'office_name': 'District 10', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-10', 'office_address': '1976 East Dr. Martin Luther King Jr. Blvd.', 'office_city': 'Stockton', 'office_state': 'CA', 'office_zip': '95205', 'office_phone': '(209) 948-7543', 'mail_address': '1976 East Dr. Martin Luther King Jr. Blvd.', 'mail_pobox': None, 'mail_city': 'Stockton', 'mail_state': 'CA', 'mail_zip': '95205', 'mail_phone': None}, {'office_name': 'District 11', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-11', 'office_address': '4050 Taylor Street', 'office_city': 'San Diego', 'office_state': 'CA', 'office_zip': '92110', 'office_phone': '(619) 688-6699', 'mail_address': '4050 Taylor Street', 'mail_pobox': None, 'mail_city': 'San Diego', 'mail_state': 'CA', 'mail_zip': '92110', 'mail_phone': None}, {'office_name': 'District 12', 'office_link': 'http://www.dot.ca.gov/caltrans-near-me/district-12', 'office_address': '1750 East 4th Street, Suite 100', 'office_city': 'Santa Ana', 'office_state': 'CA', 'office_zip': '92705', 'office_phone': '(657) 328-6000', 'mail_address': '1750 East 4th Street, Suite 100', 'mail_pobox': None, 'mail_city': 'Santa Ana', 'mail_state': 'CA', 'mail_zip': '92705', 'mail_phone': None}]
        self.assertListEqual(problem_three.office_scrape(), expected_result)


if __name__ == '__main__':
    unittest.main()