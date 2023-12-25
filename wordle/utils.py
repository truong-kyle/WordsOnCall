"""
@kyle explain what this does
"""
# this is what i meant by collections package
from collections import Counter

def get_words_from_file(file_path):
    """
    @kyle explain what this does
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read().split()

# Your function is redundant, you can just use Counter() directly
# keeping it here for reference
def count_letters(word):
    """
    @kyle explain what this does
    """
    return Counter(word)
