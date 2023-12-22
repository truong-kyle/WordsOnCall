import random

def readFile(file_path: str):
    with open(file_path, 'r') as file:
        text = file.read()
        lines = text.split()
    return lines

def countLetters(word: str):
    wordDict = {}
    for letter in word:
        if letter in wordDict:
            wordDict[letter] += 1
        else:
            wordDict[letter] = 1
    return wordDict

def checkInt(x: str):
    try:
        y = int(x)
        if(y<4 or y>7):
            raise ValueError
        
    except ValueError:
        print("Invalid Value, Try Again")
        return False
    else:
        return True

class Wordle:

    def __init__(self, num: int) -> None:
        self.wordLen = num
        self.wordbank = readFile(f'words/{self.wordLen}letters.txt')
        self.chosenWord = random.choice(self.wordbank).lower()
        self.letterBank = {}
        pass

    def solve(self, guess: str):
        guessTuple = []
        wordDict = countLetters(self.chosenWord)
        for i in range(self.wordLen):
            if guess[i] in wordDict and wordDict[guess[i]] != 0:
                if(guess[i]==self.chosenWord[i]):
                    guessTuple.append((guess[i], 2))
                else:
                    guessTuple.append((guess[i], 1))
                wordDict[guess[i]] -= 1
            else:
                guessTuple.append((guess[i], 0))
            self.updateBank(guessTuple)
        return guessTuple
    
    def updateBank(self, tupleList: list):
        for letterTup in tupleList:
            if not(letterTup[0] in self.letterBank):
                self.letterBank[letterTup[0]] = letterTup[1]
            elif letterTup[1] > self.letterBank[letterTup[0]]:
                self.letterBank[letterTup[0]] = letterTup[1]
        self.letterBank = dict(sorted(self.letterBank.items()))
 



if __name__ == "__main__":
    getLen = input("Word Length: ")
    reqLen = int(getLen) if getLen.isnumeric() and int(getLen) >= 4 and int(getLen) <= 7 else random.randint(4, 7)
    game = Wordle(reqLen)
    win = False
    count = 0
    while count in range(0, reqLen+1):
        print(count)
        guessWord = input(f'Enter a {reqLen} length word: ')
        if len(guessWord) == reqLen:
            if guessWord in game.wordbank:
                count += 1
                res = game.solve(guessWord)
                print(f'{game.letterBank}\n{res}')
                if guessWord == game.chosenWord:
                    break
            else:
                    print('Word not in wordbank')
        else:
            print(f'Word must be a {reqLen} long word')
    print(game.chosenWord)
    input("")