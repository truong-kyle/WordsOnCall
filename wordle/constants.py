"""
@kyle read game.py to see wha to write here
"""

from enum import Enum, unique
# Did you know python has a built-in enum class?
#  It's pretty cool no need to return 0 1 2 xD like a C programmer >.<
# but you ask what are enums? well ddg it.

@unique
class GuessStatus(Enum):
    """
    This is an enum class for the status of a guess.
    Enums are very cool and you should use them more often.
    They are amazing for the match function
    Since they are descriptive and easy to read unlike numbers 0 1 2
    THE NUMBERS MASON WHAT DO THEY MEAN?!
    """
    CORRECT = 2
    PRESENT = 1
    ABSENT = 0

@unique
class ValidateStatus(Enum):
    """
    Likewise xD
    """
    VALID = 0
    NOT_IN_WORD_BANK = 1
    WRONG_LENGTH = 2
    ALREADY_GUESSED = 3

ALLOWED_WORD_LENGTHS = [4, 5, 6, 7, 8]

DEFAULT_WORD_LENGTH = 5

MAX_GUESSES = 8

GUESS_STATUS = {
    'correct': 2,
    'present': 1,
    'absent': 0
}
