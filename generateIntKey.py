import saveKey, random
def generateKey(keyLength, iter, round):
    permutation = []
    while len(permutation) < keyLength:
        number = random.randint(0, keyLength - 1)
        if number not in permutation:
            permutation.append(number)

    # Запись ключа в файл
    saveKey.saveKey(permutation, "Permutation", round, iter)
    return permutation