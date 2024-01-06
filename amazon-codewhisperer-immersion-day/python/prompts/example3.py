"""
Function that takes a list that contains some numbers and strings, format them
into a string in which the numbers are prepended with a '#' and the strings
are wrapped in double quotes
"""


def format_list(lst):
    """
    Formats a list of numbers and strings into a string
    """
    result = ""
    for i, item in enumerate(lst):
        if isinstance(item, int):
            result += f"#{item}"
        elif isinstance(item, str):
            result += f'"{item}"'
        if i < len(lst) - 1:
            result += ", "
    return result
