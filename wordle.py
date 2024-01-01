import config, random
class Wordle:

    def __init__(self, num: int) -> None:
        self.wordLen = num
        self.wordbank = config.readFile(f'words/{self.wordLen}letters.txt')
        self.chosenWord = random.choice(self.wordbank).lower()
        self.letterBank = {}
        pass

    def solve(self, guess: str):
        guessTuple = []
        wordDict = config.countLetters(self.chosenWord)
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