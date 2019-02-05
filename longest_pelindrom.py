"find the all and longest pelindrome from the string"

def palindromes(text):
    results = []
    for i in range(len(text)):
        for j in range(0, i):
            part = text[j:i + 1]

            if part == part[::-1]:
                results.append(part)

    return max(results, key=len), results




text="aabsmsabccba"
print(palindromes(text))
    