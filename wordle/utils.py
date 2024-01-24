"""
Loads the words from the .txt file into memory
"""
# this is what i meant by collections package
from collections import Counter

def get_words_from_file(file_path):
    """
    Opens the file from the requested path and splits by line.
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
