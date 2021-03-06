"""Functions that create copies of characters and strings"""

# Source and/or inspiration for function(s):
# http://whatcanbecomputed.com/

LETTER_C = "C"


def mcopies_ofc(input_string):
    """Create copy_count (number in input_string) copies of the letter 'C'"""
    copy_count = int(input_string)
    list_of_letter_c = []
    # iterate copy_count times, appending a 'C' character at each iteration
    # pylint: disable=unused-variable
    for i in range(copy_count):
        list_of_letter_c.append(LETTER_C)
    # join all the C's together into a single string, with no separator
    return "".join(list_of_letter_c)


def mcopies_of(input_string, character):
    """Create copy_count (number in input_string) copies of the character"""
    copy_count = int(input_string)
    list_of_letter = []
    # iterate copy_count times, appending a character at each iteration
    # pylint: disable=unused-variable
    for i in range(copy_count):
        list_of_letter.append(character)
    # join all the letters together into a single string, with no separator
    return "".join(list_of_letter)
