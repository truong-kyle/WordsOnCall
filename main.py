import random, wordle

def validateWord(word: str) -> int:
    if len(word) == reqLen:
          if guessWord in game.wordbank: return 0
          else: return 1
    else: return 2

if __name__ == "__main__":
    getLen = input("Word Length: ")
    reqLen = int(getLen) if getLen.isnumeric() and int(getLen) >= 4 and int(getLen) <= 7 else random.randint(4, 7)
    game = wordle.Wordle(reqLen)
    count = 0
    while count in range(0, reqLen+1):
        print(count)
        guessWord = input(f'Enter a {reqLen} length word: ')
        match validateWord(guessWord):
            case 0:
                count += 1
                print(f'{game.solve(guessWord)}\n{game.letterBank}')
                if guessWord == game.chosenWord: break
            case 1: print('Word not in wordbank')
            case 2: print(f'Word must be a {reqLen} long word')            
    print(game.chosenWord)
    input("")