import wordle as game

count = 0
guess = ""
result = False
secret, wordbank = game.getWord()
letterBank = {}
while not(result) and count <= len(secret):
    print(f"Guesses left: {len(secret) + 1 - count}")
    guess = input(f"Enter a {len(secret)} letter word: ").lower()
    if guess.isalpha() and len(guess) == len(secret):
        if guess in wordbank:
            count += 1
            result, guessRes = game.solve(secret, guess)
            letterBank = game.updateBank(guessRes, letterBank)
            print(f'\nLetters used:\n{letterBank}')
            game.colourLetter(guessRes)
        else:
            print("Word not in wordbank")
    else:
        print(f"Guesses must be a {len(secret)} letter word")
print(secret)
print("You Win!" if count<=len(secret) else "You Lose!")
input()

