"""
@kyle
Good practice to add a docstring to every file on top to tell user , what it does.
One line is enough but you can add more if you want.
Like this one. xD
"""
from random import choice as word_picker
#                      ^^^^^^^
# this is bad practice (it might confuse other maintainers)
# but i wanted to show you that you can rename imports (weird flex but okay)

from .utils import get_words_from_file, count_letters
from .constants import GuessStatus, ValidateStatus


class Wordle:
    """
    @kyle explain what this does
    """
    def __init__(self, word_length):
        self.word_length = word_length
        self.word_bank = get_words_from_file(f'data/words/{self.word_length}letters.txt')
        self.chosen_word = word_picker(self.word_bank).lower()
        self.letter_bank = {}
        self.past_guesses = [] # (wordle works this way) (analyze why this is needed)
        print(f"DEBUG ONLY - Chosen word: {self.chosen_word} + length: {self.word_length}")

    def validate_word(self, guess):
        """
        @kyle explain what this does
        """
        if len(guess) != self.word_length:
            return ValidateStatus.WRONG_LENGTH

        if guess not in self.word_bank:
            return ValidateStatus.NOT_IN_WORD_BANK

        if guess in self.past_guesses:
            return ValidateStatus.ALREADY_GUESSED

        return ValidateStatus.VALID

    def solve(self, guess):
        """
        @kyle explain what this does
        """
        # Why did i append the guess here instead of end of validate_word funciton?
        # -> HINT: SRP
        self.past_guesses.append(guess)

        guess_result = []
        # You can use python's built-in counter from collecions
        word_dict = count_letters(self.chosen_word)

        # python-ick way to iterate over a list no need to use range like a rover.
        for i, letter in enumerate(guess):
            # Ideally you'd use .get() here but I'll leave that for you to figure out.
            # Question yourself what is .get() and why .get() over [x]?
            # (get it 'get over ex'.. no ok)
            # hint: word_dict.get()
            if letter in word_dict and word_dict[letter] > 0:
                if letter == self.chosen_word[i]:
                    status = GuessStatus.CORRECT
                else:
                    status = GuessStatus.PRESENT
                word_dict[letter] -= 1
            else:
                status = GuessStatus.ABSENT

            guess_result.append((letter, status.value))

        self.update_letter_bank(guess_result)
        return guess_result

    def update_letter_bank(self, guess_result):
        """
        @kyle explain what this does
        """
        # You can unpack a tuple into two variables like this
        # a, b = (1, 2)
        # a = 1 and b = 2
        for letter, status in guess_result:
            # I genuinly don't know why you used elif before but i guess you're tired.
            # \ is used to escape a newline character #orgainseyourcodebetter #pep8
            if letter not in self.letter_bank \
                or status > self.letter_bank[letter]:
                self.letter_bank[letter] = status

        self.letter_bank = dict(sorted(self.letter_bank.items()))
