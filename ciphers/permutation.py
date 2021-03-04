import random
import generateIntKey
import grouper
import math

lengthBlock = 256  # Длина перестановки ( блока )


def encodePermutation(text, iter, round):

    textSize = len(text)

    # Рандомное генерирование ключа перестановки
    if textSize > lengthBlock:
        permutation = generateIntKey.generateKey(lengthBlock, iter, round)
    else:
        permutation = generateIntKey.generateKey(textSize, iter, round)

    textBlocks = grouper.grouper(text, lengthBlock)

    countBlocks = math.ceil(textSize / lengthBlock)

    stringNewText = ""
    # Собственно сама перестановка
    count = 0
    for i in range(int(countBlocks)):

        text = list(textBlocks[i])
        newText = []  # Массив для нового текста
        textSize = len(text)  # Длина дополненной строки
        count += textSize
        for j in range(textSize):
            try:
                newText.append(text[permutation[j]])
            except IndexError:
                print("Permutation Encode Index Error")
        stringNewText += ''.join(newText)

    return stringNewText

def decodePermutation(encodeText, key):
    textSize = len(encodeText)

    textBlocks = grouper.grouper(encodeText, lengthBlock)

    countBlocks = math.ceil(len(textBlocks))

    stringOldText = ""
    for i in range(int(countBlocks)):
        text = list(textBlocks[i])

        oldText = [""] * lengthBlock  # Массив для нового текста
        textSize = len(text)  # Длина дополненной строки
        for j in range(textSize):
            try:
                oldText.pop(int(key[j]))
                oldText.insert(int(key[j]), text[j])
            except IndexError:
                print("Permutation Decode Index Error")
        stringOldText += ''.join(oldText)

    return stringOldText
