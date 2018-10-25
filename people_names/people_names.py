# coding: utf-8
import re
import unidecode
from functools import reduce
from slugify import Slugify
from people_names import stakeholder_positions
from people_names import nickname_override
from people_names import post_nominals

# name_format:
# fml  ==> first middle last
# lfm  ==> last first middle

def normalize_string(u_str):
    return unidecode.unidecode(u_str)

def slugify_string(str):
    my_slugify = Slugify()
    my_slugify.to_lower=True
    return my_slugify(str)

def add_name_parts_to_dict(obj, name_parts):
    obj['first_name'] = name_parts['first_name']
    obj['middle_name'] = name_parts['middle_name']
    obj['last_name'] = name_parts['last_name']
    obj['suffix_name'] = name_parts['suffix_name']
    obj['nominal_name'] = name_parts['nominal_name']
    obj['nickname'] = name_parts['nickname']
    obj['slug_name'] = name_parts['slug_name']

def split_name(name_str, name_format, force_split=False): # force_split - add comma if none and return result for (l, f m)
    if name_str == '':
        return {'first_name': '',
                'middle_name': '',
                'last_name': '',
                'suffix_name': '',
                'nominal_name': '',
                'nickname': '',
                'slug_name': ''
        }

    name_str = normalize_string(name_str)
    name_str = _strip_stakeholder_positions(name_str)
    name_str = _reformat_stakeholder_nominal(name_str)
    name_str = name_str.strip()

    if name_format == 'lfm':
        return _process_last_middle_first(name_str, force_split)
    elif name_format == 'fml':
        return _process_first_middle_last(name_str)
    else:
        return {"err": "invalid name format..."}


def _process_first_middle_last(name_str):
    names = {'original_name': name_str}
    name_str = _first_name(name_str)
    name_str = re.sub(',is$','', name_str)
    name_str = name_str.replace(".", "")
    name_str = name_str.replace("*", "")
    name_str = name_str.replace(",", " ")
    name_str = re.sub('\s+',' ', name_str) # done for things like: john smith , jr <-- extra space before comma


    name_arr = name_str.split(" ")
    # print (name_arr)
    nominal_results = _check_and_remove_nominal(name_arr)
    nickname_results = _check_for_nickname_new(nominal_results['arr'])
    name_arr = nickname_results['arr']
    # print (name_arr)
    suffix_name = get_suffix_name(name_arr)
    # print (name_arr)
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

    middle_name, last_name = _check_middle_last_name(middle_name, last_name)

    names = {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name}

    names['nickname'] = nickname_results['nickname']
    names['nominal_name'] = nominal_results['nominal_name']
    names['suffix_name'] = suffix_name
    names['slug_name'] = _slugify_name(names) # don't pass first element (first_name)
    return names

def _process_last_middle_first(name_str, force_split):
    if force_split:
        name_str = _check_for_comma(name_str) # check that there's a comma after last name
    name_str = _strip_remaining_same_chars(name_str, ',')
    name_str = _ensure_space_after_comma(name_str)


    name_str = name_str.replace(".", "")
    name_str = name_str.title() # convert to upper/lowercase



    name_arr = name_str.rsplit(", ", 1)
    if len(name_arr) > 1:
        names = _get_last_middle_first(name_arr)
    else:
        return None
    return names

def _check_for_comma(str):
    str_split = str.split()
    if str_split[0].endswith(','):
        return str
    else:
        return ', '.join(str_split)

def _get_last_middle_first(name_arr):
    names = {}
    names['last_name'] = name_arr[0]
    name_arr = (name_arr[1]).split(" ")
    results = _check_and_remove_nominal(name_arr)
    nominal_results = _check_and_remove_nominal(name_arr)
    nickname_results = _check_for_nickname_new(nominal_results['arr'])
    name_arr = nickname_results['arr']
    names['nickname'] = nickname_results['nickname']
    names['nominal_name'] = nominal_results['nominal_name']
    names['suffix_name'] = get_suffix_name(name_arr)
    names['first_name'] = _get_first_element(name_arr)
    names['middle_name'] = _get_join_elements(name_arr[1:]) # don't pass first element (first_name)

    names['slug_name'] = _slugify_name(names) # don't pass first element (first_name)

    ## done if suffix_name in last name vs end of first/middle
    if names['suffix_name'] == '':
        name_arr = (names['last_name']).split(" ")
        names['suffix_name'] = get_suffix_name(name_arr)
        names['last_name'] = _get_join_elements(name_arr)

    return names

def _slugify_name(name):
    return slugify_string(name['first_name'] + ' ' + name['middle_name'] + ' ' + name['last_name'])

# fix for things like Mr.John smith
def _first_name(name_str):
    name = name_str
    match = re.search(r'^(Mr|Ms|Dr)\.(\S.*)', name_str, re.IGNORECASE)
    if match:
        name = "%s %s" % (match.group(1), match.group(2))
    return name

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

def _check_for_nickname_new(name):
    full_name = ' '.join(name)
    nickname = _check_nickname(full_name)
    return nickname

# remove trailing characters after first occurance (done for Torkelson, Paul, M - remove 2nd comma)
def _strip_remaining_same_chars(str, char):
    first_comma_idx = str.find(char)
    strip_comma_string = str[first_comma_idx+1:].replace(char, "")
    return str[:first_comma_idx+1] + strip_comma_string

# check if name like last_name,first_name (no space after comma)
def _ensure_space_after_comma(str):
    return re.sub(',(?=\S)', ', ', str)


# TODO: this is the worst... fix this sometime...
def _check_middle_last_name(middle_name, last_name):
    middle_name_arr = middle_name.split(" ")
    if len(middle_name_arr) > 1:
        middle = middle_name_arr[0]
        last = last_name
        for idx, m_name in enumerate(middle_name_arr[1:]):
            if len(m_name) == 1:
                middle = '{} {}'.format(middle, m_name)
            else:
                last = '{} {}'.format(m_name, last)

        middle_name = re.sub('\s+', ' ', middle.strip())
        last_name = re.sub('\s+', ' ', last.strip())

    return [middle_name, last_name]

def _check_nickname(name):
    nickname = ''
    nickname_stripped = name
    match = re.search(r'(.*?)(\(|\")(.*)(\)|\")(.*)', name, re.IGNORECASE)
    if match:
        nickname_stripped = match.group(1) + ' ' + match.group(5)
        nickname_stripped = re.sub('\s+',' ', nickname_stripped.strip())

        nickname = _check_nickname_override(match.group(3))
        nickname = nickname.replace("\'", "")
        nickname = nickname.replace("\"", "")
    return {'nickname': nickname, 'arr': nickname_stripped.split(" ")}

def _determine_last_name_prefix(names_arr):
    full_name = ' '.join(names_arr)
    prefixes = ['del', 'van', 'de', 'st', 'da', 'di', 'la', 'le', 'von', 'della', 'du']
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

def _check_and_remove_nominal(names):
    names_no_post_nominal = []
    nominal_name = ''
    for name in names:
        nominal_name_new = _check_post_nominal(name)
        if nominal_name_new == '':
            names_no_post_nominal.append(name)
        nominal_name = _determine_set_name('nominal', nominal_name, nominal_name_new)

    return {'arr': names_no_post_nominal, 'nominal_name': nominal_name}

def _determine_set_name(name_type, name, name_new):
    if name_type == 'nickname':
        name_new = _check_nickname_override(name_new)
    if name == '':
        return name_new
    else:
        return name

def _check_nickname_override(nickname):
    nicknames = nickname_override.get()
    for nick in nicknames:
        if nickname.lower() == nick:
            return ''
    return nickname

def _strip_stakeholder_positions(name_str):
    positions = stakeholder_positions.get()
    return reduce(lambda a, pos: a.replace(pos, ''), positions, name_str)

def _reformat_stakeholder_nominal(name_str):
    name_str = name_str.replace("P. Eng.", "P.Eng.")

    return name_str.strip()

def _check_post_nominal(name):
    post_nominal_names = post_nominals.get()
    lowercase_name = name.lower()
    post_nominal = ''
    for pn in post_nominal_names:
        if pn[0] == lowercase_name:
            return pn[1]
            
    if re.match(r'^bsc\s?\(.*\)$', name, re.IGNORECASE):
        post_nominal = 'BSc'
    elif re.match(r'^msc\s?\(.*\)$', name, re.IGNORECASE):
        post_nominal = 'MSc'
    elif re.match(r'^Gen\s?\(Retd\)$', name, re.IGNORECASE):
        post_nominal = 'Gen'
    
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

    if len(names) != 0:
        names[-1] = str.rstrip(names[-1], ',') # strip trailing comma if any from last name
    return suffix_name
