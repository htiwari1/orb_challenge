import re


def clean_names(raw_names):
    characters_to_remove_list = ['***', '*', '. ', ' .', '.,', '(', ')', ':', '|', ', -']
    split_dba_regex = 'DBA|D. B. A.|D.B.A.|dba|dba.|d-b-a|d.b.a|/D.B.A./'

    result = []
    for i in raw_names:

        split_arr = re.split(split_dba_regex, i)
        company_legal_name = (split_arr[0])
        if len(split_arr) > 1:
            company_dba_name = (split_arr[1])
        else:
            company_dba_name = ''

        for ch in characters_to_remove_list:
            if ch in company_dba_name:
                company_dba_name = company_dba_name.replace(ch, '')
            if ch in company_legal_name:
                company_legal_name = company_legal_name.replace(ch, '')

        company_dba_name = company_dba_name.replace('_', ' ')

        if len(company_legal_name) > 0 and company_legal_name[0] in ['/', ',']:
            company_legal_name = company_legal_name[1:]
        if len(company_legal_name) > 0 and company_legal_name[-1] in ['/', ',']:
            company_legal_name = company_legal_name[:-1]

        if len(company_dba_name) > 0 and company_dba_name[0] in ['/', ',']:
            company_dba_name = company_dba_name[1:]
        if len(company_dba_name) > 0 and company_dba_name[-1] in ['/', ',']:
            company_dba_name = company_dba_name[:-1]

        company_legal_name = (company_legal_name.replace('LLC,', 'LLC').strip())
        company_dba_name = (company_dba_name.strip())

        if company_dba_name == '':
            company_dba_name = None

        result.append((company_legal_name, company_dba_name))

    return result


if __name__ == "__main__":
    RAW_NAMES = [
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

    CLEANED_NAME_PAIRS = [
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

    try:
        assert clean_names(RAW_NAMES) == CLEANED_NAME_PAIRS
    except AssertionError:
        print(clean_names(RAW_NAMES))
