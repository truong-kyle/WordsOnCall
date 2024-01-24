"""
@kyle explain what this does
"""
from wordle.game import Wordle
from wordle.constants import  DEFAULT_WORD_LENGTH, ALLOWED_WORD_LENGTHS, MAX_GUESSES, ValidateStatus

def main():
    """
    @kyle explain what this does
    """
    # I've streamlined the code a bit, but it's still not as clean as I'd like.
    user_input = input("Enter word length or press enter for default: ").strip()
    if user_input == '':
        user_input = str(DEFAULT_WORD_LENGTH)
    else:
        if not user_input.isnumeric():
            print("Word length must be a number")
            main()

    word_length = int(user_input)
    # Your < 4 and > 7 check is okay but
    # what if I want a word of length 8 and 10 but exclude 9 (because 7 .. yk ate it)
    if word_length not in ALLOWED_WORD_LENGTHS:
        print(f"Word length must be one of {ALLOWED_WORD_LENGTHS}")
        main()

    # OOP..s
    game = Wordle(word_length)

    # I've added a play_count variable to keep track of the number of guesses.
    play_count = 0

    # I've removed the count variable and replaced it with a while True loop and a break statement.
    # This is a bit more pythonic and easier to read. (some weird python dude said this not me)
    while True:
        # It's good practice to have break statements on the top of the loop
        # so that you don't have to scroll down to see what the condition is.
        # but this is just my opinion.
        if play_count > MAX_GUESSES:
            print("You've run out of guesses!")
            break


        # Now it shows the number of remaining guesses
        guess = input(f"{play_count}/{MAX_GUESSES} Enter your guess: ")

        #  let's validate the word shall we? Fulcrum come in.... (I'm sorry)
        validate_result = game.validate_word(guess)
        # Much better than using 1, 2, 3, 4 xD (imo)
        # Also see how fun it is to add new validate statuses? (I added ALREADY_GUESSED)
        match validate_result:
            case ValidateStatus.WRONG_LENGTH:
                print(f"{guess} is not the correct length")
                continue
            case ValidateStatus.NOT_IN_WORD_BANK:
                print(f"{guess} is not in the word bank")
                continue
            case ValidateStatus.ALREADY_GUESSED:
                print(f"{guess} has already been guessed")
                continue
            case ValidateStatus.VALID:
                # Only increment play_count if the word is valid
                play_count += 1

        # WE USE OOP !!!
        result = game.solve(guess)

        print(result)


if __name__ == "__main__":
    getLen = input("Word Length: ")
    reqLen = int(getLen) if getLen.isnumeric() and int(getLen) >= 4 and int(getLen) <= 7 else random.randint(4, 7)
    game = wordle.Wordle(reqLen)
    count = 0
    while count in range(0, reqLen+1):
        print(f'Guesses remaining: {reqLen+1-count}')
        guessWord = input(f'Enter a {reqLen} length word: ')
        match validateWord(guessWord):
            case 0:
                count += 1
                print(f'{game.solve(guessWord)}\nLetters used: {game.letterBank.keys()}')
                if guessWord == game.chosenWord: break
            case 1: print('Word not in wordbank')
            case 2: print(f'Word must be a {reqLen} long word')            
    print(game.chosenWord)

