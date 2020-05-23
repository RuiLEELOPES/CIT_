number = 1
limit = 1000000000000

print("369369 369369")
while number < limit :
    exponent = 1
    count = 0
    while number > 10 ** (exponent -1):
        determinant = ((number % (10 ** exponent)) - (number % 10**(exponent -1))) / (10 ** (exponent -1))
        if((determinant % 3 == 0) and (determinant != 0)):
            count = count + 1
        exponent = exponent + 1

    if (count == 0):
        print(number)
    else :
        countchak = 0
        while countchak < count :
            print("짝", end = "")
            countchak = countchak + 1
        print("")

    number = number + 1
