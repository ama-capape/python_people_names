import re
# name_format:
# fml  ==> first middle last
# lmf  ==> last middle first

def add_name_parts_to_dict(obj, name_parts):
    obj['first_name'] = name_parts['first_name']
    obj['middle_name'] = name_parts['middle_name']
    obj['last_name'] = name_parts['last_name']
    obj['suffix_name'] = name_parts['suffix_name']
    obj['nominal_name'] = name_parts['nominal_name']
    obj['nickname'] = name_parts['nickname']

def split_name(name_str, name_format):
    if name_str == '':
        return {'first_name': '', 'middle_name': '', 'last_name': '', 'suffix_name': '', 'nominal_name': '', 'nickname': ''}

    if name_format == 'lmf':
        return _process_last_middle_first(name_str)
    elif name_format == 'fml':
        return _process_first_middle_last(name_str)


def _process_first_middle_last(name_str):
    names = {}
    name_arr = name_str.split(" ")
    print name_arr
    results = _check_and_remove_nominal_and_nickname(name_arr)
    name_arr = results['arr']

    suffix_name = get_suffix_name(name_arr)
    print name_arr
    names = _determine_name_if_last_name_has_prefix(name_arr)

    if not names:
        last_name = name_arr[-1]
        first_name = _get_first_element(name_arr[:-1])
        middle_name = _get_join_elements(name_arr[1:-1])
        names = {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}

    names['nickname'] = results['nickname']
    names['nominal_name'] = results['nominal_name']
    names['suffix_name'] = suffix_name
    return names

def _process_last_middle_first(name_str):
    name_str = name_str.title() # convert to upper/lowercase
    names = {}
    name_arr = name_str.split(", ")
    names['last_name'] = name_arr[0]
    name_arr = (name_arr[1]).split(" ")
    results = _check_and_remove_nominal_and_nickname(name_arr)
    name_arr = results['arr']
    names['nickname'] = results['nickname']
    names['nominal_name'] = results['nominal_name']
    names['suffix_name'] = get_suffix_name(name_arr)


    names['first_name'] = _get_first_element(name_arr)
    names['middle_name'] = _get_join_elements(name_arr[1:]) # don't pass first element (first_name)

    ## done if suffix_name in last name vs end of first/middle
    if names['suffix_name'] == '':
        name_arr = (names['last_name']).split(" ")
        names['suffix_name'] = get_suffix_name(name_arr)
        names['last_name'] = _get_join_elements(name_arr)

    return names

def _determine_name_if_last_name_has_prefix(name_arr):
    names = {}

    if len(name_arr) >= 3:
        names = _check_3_or_more_last_name(name_arr)

    if not names and len(name_arr) >= 2:
        names = _check_2_or_more_last_name(name_arr)

    return names

def _check_3_or_more_last_name(name_arr):
    if re.match(r'^van$', name_arr[-3], re.IGNORECASE) and re.match(r'^der$', name_arr[-2], re.IGNORECASE):
        first_name = _get_first_element(name_arr[:-3])
        middle_name = _get_join_elements(name_arr[1:-3])
        last_name = name_arr[-3] + ' ' + name_arr[-2] + ' ' + name_arr[-1]
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}

    if re.match(r'^de$', name_arr[-3], re.IGNORECASE) and re.match(r'^saint$', name_arr[-2], re.IGNORECASE):
        first_name = _get_first_element(name_arr[:-3])
        middle_name = _get_join_elements(name_arr[1:-3])
        last_name = name_arr[-3] + ' ' + name_arr[-2] + ' ' + name_arr[-1]
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    return None

def _check_2_or_more_last_name(name_arr):
    if re.match(r'^van$', name_arr[-2], re.IGNORECASE):
        last_name = name_arr[-2] + ' ' + name_arr[-1]
        first_name = _get_first_element(name_arr[:-2])
        middle_name = _get_join_elements(name_arr[1:-2])
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    elif re.match(r'^von$', name_arr[-2], re.IGNORECASE):
        first_name = _get_first_element(name_arr[:-2])
        middle_name = _get_join_elements(name_arr[1:-2])
        last_name = name_arr[-2] + ' ' + name_arr[-1]
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    elif re.match(r'^de$', name_arr[-2], re.IGNORECASE):
        first_name = _get_first_element(name_arr[:-2])
        middle_name = _get_join_elements(name_arr[1:-2])
        last_name = name_arr[-2] + ' ' + name_arr[-1]
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    elif re.match(r'^st(\.?)$', name_arr[-2], re.IGNORECASE):
        first_name = _get_first_element(name_arr[:-2])
        middle_name = _get_join_elements(name_arr[1:-2])
        last_name = name_arr[-2] + ' ' + name_arr[-1]
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    return None

def _get_first_element(names):
    if len(names) == 0:
        return ''
    return str.rstrip(names[0], '.')


def _get_join_elements(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return str.rstrip(names[0], '.')
        # return names[0]
    else:
        return ' '.join(names)

def _check_and_remove_nominal_and_nickname(names):
    names_no_post_nominal = []
    nickname = ''
    nominal_name = ''
    for name in names:
        nickname_new = _check_for_nickname(name)
        nominal_name_new = _check_post_nominal(name)
        if nominal_name_new == '' and nickname_new == '':
            names_no_post_nominal.append(name)

        nickname = _determine_set_name(nickname, nickname_new)
        nominal_name = _determine_set_name(nominal_name, nominal_name_new)

    return {'arr': names_no_post_nominal, 'nickname': nickname, 'nominal_name': nominal_name}


def _determine_set_name(name, name_new):
    if name == '':
        return name_new
    else:
        return name


def _check_for_nickname(name):
    nickname = _check_nickname(name)

    # override nicknames if not true nicknames
    if re.match(r'^retd.$', nickname, re.IGNORECASE):
        nickname = ''
    return nickname

def _check_nickname(name):
    nickname = ''
    match = re.search(r'^\((.*)\)$', name, re.IGNORECASE)
    if match:
        nickname = match.group(1)

    return nickname

def _check_post_nominal(name):
    post_nominal = ''
    if re.match(r'^Mr(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Mr'
    elif re.match(r'^MS(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Ms'
    elif re.match(r'^Ph(\.?)D(\.?)$', name, re.IGNORECASE):
        post_nominal = 'PhD'
    elif re.match(r'^Dr(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Dr'
    elif re.match(r'^M(\.?)D(\.?)$', name, re.IGNORECASE):
        post_nominal = 'MD'
    elif re.match(r'^J(\.?)D(\.?)$', name, re.IGNORECASE):
        post_nominal = 'JD'
    elif re.match(r'^Esq(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Esq'
    elif re.match(r'^CPA(\.?)$', name, re.IGNORECASE):
        post_nominal = 'CPA'
    elif re.match(r'^Gen(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Gen'
    elif re.match(r'^Gen(\.?)\s?\(Retd(\.?)\)(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Gen'
    elif re.match(r'^\(Retd\.\)$', name, re.IGNORECASE):
        post_nominal = 'Retd'
    elif re.match(r'^Lt(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Lt'
    elif re.match(r'^Sir(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Sir'
    elif re.match(r'^CFA(\.?)$', name, re.IGNORECASE):
        post_nominal = 'CFA'
    elif re.match(r'^Rev(\.?)$', name, re.IGNORECASE):
        post_nominal = 'Rev'
    elif re.match(r'^dvm$', name, re.IGNORECASE):
        post_nominal = 'Dmv'
    elif re.match(r'^the$', name, re.IGNORECASE):
        post_nominal = 'the'
    elif re.match(r'^Hon(\.?)(\,?)$', name, re.IGNORECASE):
        post_nominal = 'Hon'
    elif re.match(r'^Amb(\.?)(\,?)$', name, re.IGNORECASE):
        post_nominal = 'Amb'
    return post_nominal

def get_suffix_name(names):
    last_element = names[-1]
    if re.match(r'^Jr(\.?)$', last_element, re.IGNORECASE):
        del names[-1]
        suffix_name = 'Jr'
    elif re.match(r'^Sr(\.?)$', last_element, re.IGNORECASE):
        del names[-1]
        suffix_name = 'Sr'
    elif re.match(r'^II(\.?)$', last_element, re.IGNORECASE):
        del names[-1]
        suffix_name = 'II'
    elif re.match(r'^III(\.?)$', last_element, re.IGNORECASE):
        del names[-1]
        suffix_name = 'III'
    elif re.match(r'^IV(\.?)$', last_element, re.IGNORECASE):
        del names[-1]
        suffix_name = 'IV'
    elif re.match(r'^V(\.?)$', last_element, re.IGNORECASE):
        del names[-1]
        suffix_name = 'V'
    else:
        suffix_name = ''

    names[-1] = str.rstrip(names[-1], ',') # strip trailing comma if any from last name
    return suffix_name
