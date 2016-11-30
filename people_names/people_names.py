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

    name_str = name_str.strip()
    name_str = name_str.translate(None, '.')

    if name_format == 'lmf':
        return _process_last_middle_first(name_str)
    elif name_format == 'fml':
        return _process_first_middle_last(name_str)


def _process_first_middle_last(name_str):
    name_str = name_str.translate(None, ',')
    names = {}
    name_arr = name_str.split(" ")
    # print name_arr
    results = _check_and_remove_nominal_and_nickname(name_arr)
    name_arr = results['arr']
    suffix_name = get_suffix_name(name_arr)
    # print name_arr
    prefix_results = _determine_last_name_prefix(name_arr)
    if prefix_results:
        last_name = prefix_results['last_name']
        name_arr = prefix_results['first_middle'].split(" ")
        first_name = _get_first_element(name_arr)
        middle_name = _get_join_elements(name_arr[1:]) # don't pass first element (first_name)
    else:
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

def _determine_last_name_prefix(names_arr):
    full_name = ' '.join(names_arr)
    prefixes = ['del', 'van', 'de', 'st', 'da', 'di', 'la', 'le']
    for prefix in prefixes:
        results = _check_for_last_name_prefix(full_name, prefix)
        if results:
            break;
    return results

def _check_for_last_name_prefix(name_str, prefix_to_check):
    prefix_regex = r"(.*?)\b("+re.escape(prefix_to_check)+r"\b.*)"
    match = re.search(prefix_regex, name_str, re.IGNORECASE)
    if match:
        return {'first_middle': match.group(1).strip(), 'last_name': match.group(2).strip()}
    else:
        return None

def _check_and_remove_nominal_and_nickname(names):
    names_no_post_nominal = []
    nickname = ''
    nominal_name = ''
    for name in names:
        nickname_new = _check_for_nickname(name)
        nominal_name_new = _check_post_nominal(name)
        if nominal_name_new == '' and nickname_new == '':
            names_no_post_nominal.append(name)

        nickname = _determine_set_name('nickname', nickname, nickname_new)
        nominal_name = _determine_set_name('nominal', nominal_name, nominal_name_new)

    return {'arr': names_no_post_nominal, 'nickname': nickname, 'nominal_name': nominal_name}

def _determine_set_name(name_type, name, name_new):
    if name_type == 'nickname':
        name_new = _check_nickname_override(name_new)

    if name == '':
        return name_new
    else:
        return name

def _check_nickname_override(nickname):
    nickname_lowercase = nickname.lower()
    if 'retd' == nickname_lowercase:
        nickname = ''
    elif 'retired' == nickname_lowercase:
        nickname = ''
    return nickname

def _check_for_nickname(name):
    nickname = _check_nickname_parenthesis(name)
    if not nickname:
        nickname = _check_nickname_quotes(name)
    return nickname

def _check_nickname_parenthesis(name):
    nickname = ''
    match = re.search(r'^\((.*)\)$', name, re.IGNORECASE)
    if match:
        nickname = match.group(1)

    return nickname

def _check_nickname_quotes(name):
    nickname = ''
    match = re.search(r'^(\"|\')(.*)(\"|\')$', name, re.IGNORECASE)
    if match:
        nickname = match.group(2)

    return nickname

def _check_post_nominal(name):
    lowercase_name = name.lower()
    post_nominal = ''
    if 'mr' == lowercase_name:
        post_nominal = 'Mr'
    elif 'ms' == lowercase_name:
        post_nominal = 'Ms'
    elif 'mrs' == lowercase_name:
        post_nominal = 'Mrs'
    elif 'phd' == lowercase_name:
        post_nominal = 'PhD'
    elif 'dr' == lowercase_name:
        post_nominal = 'Dr'
    elif 'md' == lowercase_name:
        post_nominal = 'MD'
    elif 'jd' == lowercase_name:
        post_nominal = 'JD'
    elif 'esq' == lowercase_name:
        post_nominal = 'Esq'
    elif 'cpa' == lowercase_name:
        post_nominal = 'CPA'
    elif 'cva' == lowercase_name:
        post_nominal = 'CVA'
    elif 'cfe' == lowercase_name:
        post_nominal = 'CFE'
    elif 'cfa' == lowercase_name:
        post_nominal = 'CFA'
    elif 'cbe' == lowercase_name:
        post_nominal = 'CBE'
    elif 'cga' == lowercase_name:
        post_nominal = 'CGA'
    elif 'gen' == lowercase_name:
        post_nominal = 'Gen'
    elif 'general' == lowercase_name:
        post_nominal = 'Gen'
    elif 'con' == lowercase_name:
        post_nominal = 'Con'
    elif 'colonel' == lowercase_name:
        post_nominal = 'Con'
    elif re.match(r'^Gen\s?\(Retd\)$', name, re.IGNORECASE):
        post_nominal = 'Gen'
    elif 'retd' == lowercase_name:
        post_nominal = 'Retd'
    elif 'retired' == lowercase_name:
        post_nominal = 'Retd'
    elif 'lt' == lowercase_name:
        post_nominal = 'Lt'
    elif 'lieutenant' == lowercase_name:
        post_nominal = 'Lt'
    elif 'adm' == lowercase_name:
        post_nominal = 'Adm'
    elif 'admiral' == lowercase_name:
        post_nominal = 'Adm'
    elif 'sir' == lowercase_name:
        post_nominal = 'Sir'
    elif 'rev' == lowercase_name:
        post_nominal = 'Rev'
    elif 'reverend' == lowercase_name:
        post_nominal = 'Rev'
    elif 'prof' == lowercase_name:
        post_nominal = 'Prof'
    elif 'professor' == lowercase_name:
        post_nominal = 'Prof'
    elif 'dvm' == lowercase_name:
        post_nominal = 'Dmv'
    elif 'the' == lowercase_name:
        post_nominal = 'the'
    elif 'hon' == lowercase_name:
        post_nominal = 'Hon'
    elif 'honorable' == lowercase_name:
        post_nominal = 'Hon'
    elif 'honourable' == lowercase_name:
        post_nominal = 'Hon'
    elif 'amb' == lowercase_name:
        post_nominal = 'Amb'
    elif 'ambassador' == lowercase_name:
        post_nominal = 'Amb'
    elif 'gov' == lowercase_name:
        post_nominal = 'Gov'
    elif 'governor' == lowercase_name:
        post_nominal = 'Gov'
    elif 'sen' == lowercase_name:
        post_nominal = 'Sen'
    elif 'senator' == lowercase_name:
        post_nominal = 'Sen'

    return post_nominal

def get_suffix_name(names):
    last_element_lower = names[-1].lower()

    if 'jr' == last_element_lower:
        del names[-1]
        suffix_name = 'Jr'
    elif 'sr' == last_element_lower:
        del names[-1]
        suffix_name = 'Sr'
    elif 'ii' == last_element_lower:
        del names[-1]
        suffix_name = 'II'
    elif 'iii' == last_element_lower:
        del names[-1]
        suffix_name = 'III'
    elif 'iv' == last_element_lower:
        del names[-1]
        suffix_name = 'IV'
    elif 'v' == last_element_lower:
        del names[-1]
        suffix_name = 'V'
    elif 'vi' == last_element_lower:
        del names[-1]
        suffix_name = 'VI'
    elif 'vii' == last_element_lower:
        del names[-1]
        suffix_name = 'VII'
    elif 'viii' == last_element_lower:
        del names[-1]
        suffix_name = 'VIII'
    else:
        suffix_name = ''

    names[-1] = str.rstrip(names[-1], ',') # strip trailing comma if any from last name
    return suffix_name
