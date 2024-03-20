from math import ceil

def riffle(cards: list[int]):
    length = ceil(len(cards) / 2)
    firsthalf = cards[:length]
    secondhalf = cards[length:]

    new = []

    for i in range(len(secondhalf)):
        new.append(firsthalf[i])
        new.append(secondhalf[i])

    if len(firsthalf) > len(secondhalf):
        new.append(firsthalf[len(secondhalf)])

    return new

def main():
    i = int(input())
    l = riffle([k for k in range(i)])
    incs = 1

    while sorted(l) != l:
        incs += 1
        l = riffle(l)

    print(incs)
    

main()