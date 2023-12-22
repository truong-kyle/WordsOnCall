# OBSELETE

import random
import colorama

def checkInt(x: str):
    try:
        y = int(x)
    except ValueError:
        print("Invalid Value, Try Again")
        return False, x
    else:
        return True, y

def readFile(file_path: str):
    with open(file_path, 'r') as file:
        text = file.read()
        lines = text.split()
    return lines

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


def getWord(chars: int):
    wordLen = chars
    wordbank = readFile(f'words/{wordLen}letters.txt')
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

def colourLetter(tupleIn):
    colorama.init(autoreset=True)
    colorDef = [(0, 'red'), (1, 'yellow'), (2, 'green')]
    colorBg = {'red': colorama.Fore.RED, 'yellow': colorama.Fore.YELLOW, 'green': colorama.Fore.GREEN}

    for letter, color_index in tupleIn:
        color_name = next(color_name for index, color_name in colorDef if index == color_index)
        color_code = colorBg.get(color_name, colorama.Fore.RESET)
        print(f"{color_code}{letter}", end=' ')
    print()

def updateBank(tupleList: list, bank: dict):
    for letterTup in tupleList:
        if not(letterTup[0] in bank):
            bank[letterTup[0]] = letterTup[1]
        elif letterTup[1] > bank[letterTup[0]]:
            bank[letterTup[0]] = letterTup[1]
    
    return dict(sorted(bank.items()))
    