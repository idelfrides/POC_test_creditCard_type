import re

re_non_digits = re.compile(r'[^\d]+')


def get_digits(value):
    """
    Get all digits from input string.

    :type value: str
    
    :rtype: str
    """
    if not value:
        return ''
    return re_non_digits.sub('', str(value))