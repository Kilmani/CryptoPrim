import generateStringKey, Double, grouper

lengthBlock = 16

# def encodeGamma(text, iter, round, alphabet):
#     textLen = len(text)
#
#     # textBlocks = map(''.join, zip(*[iter(text)] * 16))
#     # Генерация ключа и запись в файл
#     gamma = generateStringKey.generateKey(textLen, iter, round, alphabet)
#     # print(gamma)
#     # Переводим в ASCII
#     asciiText = [ord(c) for c in text]
#     asciiGamma = [ord(c) for c in gamma]
#     # print(str(asciiGamma) + " encode Gamma")
#     binaryText = []
#     for i in range(len(asciiText)):
#         binaryTextBlock = int(str(bin(asciiText[i])), 2)
#         binaryGammaBlock = int(str(bin(asciiGamma[i])), 2)
#
#         if binaryTextBlock != 0:
#             binaryTextBlock = int(Double.double(binaryTextBlock), 2)
#         if binaryGammaBlock != 0:
#             binaryGammaBlock = int(Double.double(binaryGammaBlock), 2)
#
#         binaryText.append(binaryTextBlock ^ binaryGammaBlock)
#     # print(binaryText)
#     # print(str(binaryText) + " Текст в двоичной системе")
#     encodeText = ''.join(chr(e) for e in binaryText)
#
#     return encodeText
#
#
# def decodeGamma(text, gamma):
#     asciiText = [ord(c) for c in text]
#     asciiGamma = [ord(c) for c in gamma]
#     # print(gamma)
#     # print(str(asciiGamma) + " decode Gamma")
#
#     binaryText = []
#     for i in range(len(asciiText)):
#         binaryTextBlock = int(str(bin(asciiText[i])), 2)
#         binaryGammaBlock = int(str(bin(asciiGamma[i])), 2)
#         if binaryTextBlock != 0:
#             binaryTextBlock = int(Double.double(binaryTextBlock), 2)
#         if binaryGammaBlock != 0:
#             binaryGammaBlock = int(Double.double(binaryGammaBlock), 2)
#
#         binaryText.append(binaryTextBlock ^ binaryGammaBlock)
#     # print(binaryText)
#     # print(str(binaryText) + " Текст в двоичной системе")
#     decodeText = ''.join(chr(e) for e in binaryText)
#     # print(encodeText + " Закодированная строка")
#
#     return decodeText
#

def encodeGamma(text, iter, round, alphabet):
    textLen = len(text)

    textBlocks = grouper.grouper(text, lengthBlock)
    print("textBlocks", textBlocks)

    # Генерация ключа и запись в файл
    gamma = generateStringKey.generateKey(lengthBlock, iter, round, alphabet)

    # Переводим в ASCII
    asciiGamma = [ord(c) for c in gamma]

    binaryText = []

    for textBlock in textBlocks:
        asciiText = [ord(c) for c in textBlock]
        for j in range(lengthBlock):
            binaryTextBlock = int(Double.double(asciiText[j]))
            binaryGammaBlock = int(Double.double(asciiGamma[j]))
            print("jj", binaryTextBlock, binaryGammaBlock, int(binaryTextBlock) ^ int(binaryGammaBlock))

            binaryText.append(binaryTextBlock ^ binaryGammaBlock)

    print(binaryText)
    encodeText = ''.join(chr(int(e, 2)) for e in binaryText)

    return encodeText


def decodeGamma(text, gamma):
    textLen = len(text)

    textBlocks = grouper.grouper(text, lengthBlock)
    print("textBlocks", textBlocks)

    # Переводим в ASCII
    asciiGamma = [ord(c) for c in gamma]

    binaryText = []

    for textBlock in textBlocks:
        asciiText = [ord(c) for c in textBlock]
        for j in range(lengthBlock):
            binaryTextBlock = int(Double.double(asciiText[j]))
            binaryGammaBlock = int(Double.double(asciiGamma[j]))
            while len(str(binaryTextBlock)) != 8:
                binaryTextBlock = "0" + str(binaryTextBlock)
            while len(str(binaryGammaBlock)) != 8:
                binaryGammaBlock = "0" + str(binaryGammaBlock)
            binaryText.append(int(binaryTextBlock) ^ int(binaryGammaBlock))
    decodeText = ''.join(chr(int(e, 2)) for e in binaryText)

    return decodeText

