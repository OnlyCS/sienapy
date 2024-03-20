def collatz(i, c):
    if i == 1:
        return c

    if i % 2 == 0:
        return collatz(i/2, c+1)

    return collatz((3*i)+1, c+1)


def main():
    n = int(input("num: "))

    print(n, collatz(n, 0))


main()
