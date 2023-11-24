import wordle as game

count = 0
guess = ""
result = False
secret, wordbank = game.getWord()
while not(result) and count <= len(secret):
    print(f"Guesses left: {len(secret) + 1 - count}")
    guess = input(f"Enter a {len(secret)} letter word: ").lower()
    if guess.isalpha() and len(guess) == len(secret):
        if guess in wordbank:
            count += 1
            result, guessRes, matchRes = game.solve(secret, guess)
            print(f'{guessRes}\n{matchRes}')
        else:
            print("Word not in wordbank")
    else:
        print(f"Guesses must be a {len(secret)} letter word")
print(secret)
print("You Win!" if count<=len(secret) else "You Lose!")
input()