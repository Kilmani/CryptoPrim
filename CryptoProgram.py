import binascii, random, string, os, hashlib
from ciphers import gamma, rol, permutation as perm, substitution as sub


filename = input("Введите название файла ")
# filename = "crypto.docx"

file = open(filename, 'rb')
read = file.read()
readHash = hashlib.md5(read).hexdigest()
text = read

filename = filename.split(".")
filenameEncode = filename[0] + "_encode." + filename[1]
filenameDecode = filename[0] + "_decode." + filename[1]

alphabet = ''
for i in range(len(text)):
    if alphabet.find(chr(text[i])) == -1 and chr(text[i]).isalpha():
        alphabet += chr(text[i])

text = binascii.b2a_base64(read)
text = text.decode()
lenText = len(text)
difference = (len(text)) % 256
addText = ""
allDif = 256-difference
if difference != 0:     # Если строка мала для шифрования, добавляем символы
    print("Недостаточно символов", difference)
    for i in range(allDif):
        addText += random.choice(string.ascii_letters)
text += addText

print("Алфавит", alphabet, len(alphabet))   # Печатаем алфавит, составленный из начальной строки
encodeText = ""
os.system(r'nul>keysDecode.txt')
encodeHash = []
encodeHash.append(str(hashlib.md5(text.encode('utf-8')).hexdigest()) + "_One")
iter = 0
for round in range(1):
    if round == 0:
        encodeText = perm.encodePermutation(text, iter, round)
        iter += 1
        encodeHash.append(str(hashlib.md5(encodeText.encode('utf-8')).hexdigest()) + "_Perm")
        encodeText = rol.encodeRol(encodeText, iter, round)
        iter += 1
        encodeHash.append(str(hashlib.md5(encodeText.encode('utf-8')).hexdigest()) + "_Rol")
        encodeText = sub.encodeSubstitution(encodeText, alphabet, iter, round)
        iter += 1
        encodeHash.append(str(hashlib.md5(encodeText.encode('utf-8')).hexdigest()) + "_Sub")
        encodeText = perm.encodePermutation(encodeText, iter, round)
        iter += 1
        encodeHash.append(str(hashlib.md5(encodeText.encode('utf-8')).hexdigest()) + "_Perm")

    if round % 2 == 0 and round != 0:
        encodeText = perm.encodePermutation(encodeText, iter, round)
        iter += 1
        encodeText = gamma.encodeGamma(encodeText, iter, round, alphabet)
        iter += 1
        encodeText = rol.encodeRol(encodeText, iter, round)
        iter += 1
        encodeText = sub.encodeSubstitution(encodeText, alphabet, iter, round)
        iter += 1
    if round % 2 != 0:
        encodeText = perm.encodePermutation(encodeText, iter, round)
        iter += 1
        encodeText = rol.encodeRol(encodeText, iter, round)
        iter += 1
        encodeText = sub.encodeSubstitution(encodeText, alphabet, iter, round)
        iter += 1
        encodeText = perm.encodePermutation(encodeText, iter, round)
        iter += 1



encodeFile = open(filenameEncode, 'wb')
textEncode = encodeText.encode()
encodeFile.write(textEncode)
encodeFile.close()

# Декодирование
arrayKeys = []
stringKeyFile = []
encodeIteration = []
decodeCipherName = []
with open('keysDecode.txt', 'r', encoding="utf-8") as f:
    for eachLine in f:
        stringKeyFile.append(eachLine)
        fileInfoLine = eachLine.strip().split(" ", 3)
        key = [x for x in fileInfoLine[3].strip('[]').split(', ')]

        if str(key).find(",") == -1:
            key = str(key)[2:(len(key)-3)]
        cipherName = fileInfoLine[2]
        decodeCipherName.append(cipherName)
        round = int(fileInfoLine[0])
        iter = int(fileInfoLine[1])
        encodeIteration.append(iter)
        arrayKeys.append(key)

decodeCipherName.reverse()

# Дешифрование
decodeText = ""
lengthEncodeIteration = len(encodeIteration) - 1
decodeHash = []
i = 0
for iter in reversed(encodeIteration):
    cipherName = decodeCipherName[i]
    i += 1
    if iter == lengthEncodeIteration:
        if cipherName == "Permutation":
            decodeHash.append(hashlib.md5(encodeText.encode('utf-8')).hexdigest())
            decodeText = perm.decodePermutation(encodeText, arrayKeys[iter])
            decodeHash.append(str(hashlib.md5(decodeText.encode('utf-8')).hexdigest()) + "_Perm")
        elif cipherName == "Gamma":
            decodeText = gamma.decodeGamma(encodeText, ''.join(arrayKeys[iter]))
        elif cipherName == "ROL":
            decodeText = rol.decodeRol(encodeText, arrayKeys[iter])
        elif cipherName == "Sub":
            decodeText = sub.decodeSubstitution(encodeText, arrayKeys[iter], alphabet)
    if iter <= lengthEncodeIteration-1:
        if cipherName == "Permutation":
            decodeText = perm.decodePermutation(decodeText, arrayKeys[iter])
            decodeHash.append(str(hashlib.md5(decodeText.encode('utf-8')).hexdigest()) + "_Perm")
        elif cipherName == "Gamma":
            decodeText = gamma.decodeGamma(decodeText, ''.join(arrayKeys[iter]))
            decodeHash.append(str(hashlib.md5(decodeText.encode('utf-8')).hexdigest()) + "_Gamma")
        elif cipherName == "ROL":
            decodeText = rol.decodeRol(decodeText, arrayKeys[iter])
            decodeHash.append(str(hashlib.md5(decodeText.encode('utf-8')).hexdigest()) + "_Rol")
        elif cipherName == "Sub":
            decodeText = sub.decodeSubstitution(decodeText, arrayKeys[iter], alphabet)
            decodeHash.append(str(hashlib.md5(decodeText.encode('utf-8')).hexdigest()) + "_Sub")
text = decodeText[:-(256 - difference)]

text = binascii.a2b_base64(text)

decodeFile = open(filenameDecode, 'wb')
decodeFile.write(text)
decodeFile.close()

print(encodeHash)
print(decodeHash)

decodingHash = hashlib.md5(text).hexdigest()
print("Изначальный хеш", readHash)
print("Хеш расшифрованного файла", decodingHash)