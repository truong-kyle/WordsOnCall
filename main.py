import wordle as game
start = False
while not(start):
    reqLen = input("choose a word length between 4 and 7 or press 0 for a random length: ")
    start, reqLen = game.checkInt(reqLen)

count = 0
guess = ""
result = False
secret, wordbank = game.getWord(reqLen)
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
print("You Win!" if count<len(secret)+1 else "You Lose!")
input()

