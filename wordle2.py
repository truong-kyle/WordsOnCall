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
        self.wordLen = num or random.randint(4, 7)
        self.wordbank = readFile(f'words/{self.wordLen}letter.txt')
        self.chosenWord = random.choice(self.wordbank).lower()
        self.letterBank = {}
        self.wordDict = countLetters(self.chosenWord)
        pass

    def solve(self, guess: str):
        guessTuple = []
        for i in range(self.wordLen):
            if guess[i] in self.wordDict and self.wordDict[guess[i]] != 0:
                if(guess[i]==self.chosenWord[i]):
                    guessTuple.append((guess[i], 2))
                else:
                    guessTuple.append((guess[i], 1))
                self.wordDict[guess[i]] -= 1
            else:
                guessTuple.append((guess[i], 0))
        return guess == self.chosenWord, guessTuple
    
    def updateBank(self, tupleList: list):
        for letterTup in tupleList:
            if not(letterTup[0] in self.letterBank):
                self.letterBank[letterTup[0]] = letterTup[1]
            elif letterTup[1] > self.letterBank[letterTup[0]]:
                self.letterBank[letterTup[0]] = letterTup[1]
        self.letterBank = dict(sorted(self.letterBank.items()))

if __name__ == "__main__":
    getLen = input("Word Length: ")
    reqLen = int(getLen) if getLen.isnumeric() and int(getLen) >= 4 and int(getLen) <= 7 else None
    game = Wordle(reqLen)
    print(game.chosenWord)