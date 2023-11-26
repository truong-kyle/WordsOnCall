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

def getWord():
    wordLen = random.randint(4,7)
    wordbank = readFile(f'words/{wordLen}letter.txt')
    chosenWord = random.choice(wordbank).lower()
    return chosenWord, wordbank

def solve(answer: str, guess: str):
    chosenDict = countLetters(answer)
    guessTuple = []
    for i in range(len(answer)):
        if guess[i] in chosenDict and chosenDict[guess[i]] != 0:
            if(guess[i]==answer[i]):
                guessTuple.append((guess[i], 2))
            else:
                guessTuple.append((guess[i], 1))
            chosenDict[guess[i]] -= 1
        else:
            guessTuple.append((guess[i], 0))
    return guess == answer, guessTuple

def convertList(resList: list):
    result = []
    for i in resList:
        result.append(intToString(i))
    return result

def intToString(num: int):
    refDic = {0: "O", 1: "Y", 2: "X"}
    return(refDic[num])

def updateBank(tupleList: list, bank: dict):
    for letterTup in tupleList:
        if not(letterTup[0] in bank):
            bank[letterTup[0]] = letterTup[1]
        elif letterTup[1] > bank[letterTup[0]]:
            bank[letterTup[0]] = letterTup[1]
    return bank
    