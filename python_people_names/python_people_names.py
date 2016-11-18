def split_name(name_str):
    names = {}
    if name_str == '':
        return {'first_name': '', 'middle_name': '', 'last_name': '', 'suffix_name': ''}

    # special_name = special_names_override(name_str)
    # if special_name:
    #     return special_name

    name_arr = name_str.split(" ")
    suffix_name = check_suffix_name(name_arr)
    if suffix_name != '':
        name_arr = name_arr[:-1]
        name_arr[-1] = str.rstrip(name_arr[-1], ',')
        # name_arr[-1] = utils.strip_trailing_char(name_arr[-1], ',')

    names = determine_name_if_last_name_has_prefix(name_arr)
    if not names:
        last_name = name_arr[-1]
        first_name = determine_first_name(name_arr[:-1])
        middle_name = determine_middle_name(name_arr[1:-1])
        names = {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}

    names['suffix_name'] = suffix_name
    return names

def add_name_parts_to_dict(obj, name_parts):
    obj['first_name'] = name_parts['first_name']
    obj['middle_name'] = name_parts['middle_name']
    obj['last_name'] = name_parts['last_name']
    obj['suffix_name'] = name_parts['suffix_name']

def determine_name_if_last_name_has_prefix(name_arr):
    names = {}

    if len(name_arr) >= 3:
        names = check_3_or_more_last_name(name_arr)

    if not names and len(name_arr) >= 2:
        names = check_2_or_more_last_name(name_arr)

    return names

def check_3_or_more_last_name(name_arr):
    if name_arr[-3] == 'van' and name_arr[-2] == 'der':
        first_name = determine_first_name(name_arr[:-3])
        middle_name = determine_middle_name(name_arr[1:-3])
        last_name = name_arr[-3] + ' ' + name_arr[-2] + ' ' + name_arr[-1]
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    return None

def check_2_or_more_last_name(name_arr):
    if name_arr[-2] == 'van':
        last_name = name_arr[-2] + ' ' + name_arr[-1]
        first_name = determine_first_name(name_arr[:-2])
        middle_name = determine_middle_name(name_arr[1:-2])
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    elif name_arr[-2] == 'von':
        first_name = determine_first_name(name_arr[:-2])
        middle_name = determine_middle_name(name_arr[1:-2])
        last_name = name_arr[-2] + ' ' + name_arr[-1]
        return {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}
    return None

def determine_first_name(names):
    return names[0]


def determine_middle_name(names):
    if len(names) == 0:
        return ''
    if len(names) == 1:
        return names[0]
    else:
        return names.join(' ')


# def special_names_override(name):
#     if name == 'La June Montgomery Tabron':
#         return {'first_name': 'La June', 'middle_name': '', 'last_name': 'Montgomery Tabron', 'suffix_name': ''}
#     elif name == 'Mary Alice Dorrance Malone':
#         return {'first_name': 'Mary Alice', 'middle_name': 'Dorrance', 'last_name': 'Malone', 'suffix_name': ''}
#     else:
#         return None

def check_suffix_name(names):
    if names[-1] == 'Jr.':
        return 'Jr.'
    elif names[-1] == 'Sr.':
        return 'Sr.'
    elif names[-1] == 'II':
        return 'II'
    elif names[-1] == 'III':
        return 'III'
    elif names[-1] == 'IV':
        return 'IV'
    elif names[-1] == 'V':
        return 'V'
    else:
        return ''
