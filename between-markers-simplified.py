import re

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    result = re.search('\\' + begin + '(.*)\\' + end, text)
    return (result.group(1))


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
