**Intro:**
people_names is a module that takes a string name and returns a name dict (first, middle, last, etc).

**Method:**
  name_str: the name as a string
  name_format: <lfm | fml>  (last first middle | first middle last)

**Returns**
  a name object
    {
      first_name: str,
      middle_name: str,
      last_name: str,
      suffix_name: str,
      nominal_name: str,
      nickname: str,
      slug_name: str,
    }

# unittest
* docker run -it -v ${PWD}:/usr/src/app --rm py/people-names python3 -m unittest discover -s tests -p "*_tests.py"
* docker run -it -v ${PWD}:/usr/src/app --rm py/people-names python3 -m unittest tests/fec_names_tests.py
