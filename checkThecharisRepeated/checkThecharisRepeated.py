def compareString(giveMeString):
    counts = {}
    for char in giveMeString:
        if char in counts:
            return char
        counts[char] = 1
    return None


print(compareString("ACBD"))