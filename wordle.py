import random

def readFile(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        lines = text.split()
    return lines

def countLetters(word):
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

def solve(answer, guess):
    chosenDict = countLetters(answer)
    match = []
    guessList = []
    for i in range(len(answer)):
        guessList.append(guess[i])
        if guess[i] in chosenDict and chosenDict[guess[i]] != 0:
            if(guess[i]==answer[i]):
                match.append("X")
            else:
                match.append("Y")
            chosenDict[guess[i]] -= 1
        else:
            match.append("O")
    return guess == answer, guessList, match