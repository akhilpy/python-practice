def EqualNumbers(a, n):
    for i in range(0, n):

        # Divide number by 2
        while a[i] % 2 == 0:
            a[i] //= 2

        # Divide number by 3
        while a[i] % 3 == 0:
            a[i] //= 3

    # Remaining numbers
    for i in range(1, n):
        if a[i] != a[0]:
            return False

    return True


print(EqualNumbers([2,5], 2))
