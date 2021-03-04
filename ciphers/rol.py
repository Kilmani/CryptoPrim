import saveKey, random, Double, grouper, math

lengthBlock = 8

def encodeRol(text, iter, round):
    # Генерация ключа и запись в файл
    key = 1
    saveKey.saveKey(key, "ROL", round, iter)
    # Переводим в ASCII
    asciiText = [ord(c) for c in text]

    binaryText = []
    for i in range(len(asciiText)):
        binaryTextBlock = int(Double.double(asciiText[i]))
        while len(str(binaryTextBlock)) != 8:
            binaryTextBlock = "0" + str(binaryTextBlock)
        binaryText.append(binaryTextBlock)

    encodeText = ""
    for i in binaryText:
        temp = i
        temp = shifttext(temp, 1)
        temp = ''.join(e for e in temp)
        encodeText += temp

    encodeText = grouper.grouper(encodeText, lengthBlock)
    encodeText = ''.join(chr(int(e, 2)) for e in encodeText)

    return encodeText


def decodeRol(text, key):
    # Переводим в ASCII
    asciiText = [ord(c) for c in text]
    binaryText = []
    for i in range(len(asciiText)):
        binaryTextBlock = int(Double.double(asciiText[i]))
        while len(str(binaryTextBlock)) != 8:
            binaryTextBlock = "0" + str(binaryTextBlock)
        binaryText.append(binaryTextBlock)

    decodeText = ""
    for i in binaryText:
        temp = i
        # count += len(str(temp))
        temp = shifttext(temp, -1)
        temp = ''.join(e for e in temp)
        decodeText += temp

    decodeText = grouper.grouper(decodeText, lengthBlock)
    decodeText = ''.join(chr(int(e, 2)) for e in decodeText)

    return decodeText

def shifttext(lst, steps):
    lst = list(str(lst))
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst