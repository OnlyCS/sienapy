import math


def pref_normal(n):
    max = math.ceil(math.cbrt(n))

    for start in range(1, max+1):
        total = 0
        i = start

        while total < n:
            total += i**3
            i += 1

        if total == n:
            if start == 1:
                print(n, "\tperfect\t", start, i-1)
            else:
                print(n, "\tnormal\t", start, i-1)


def near(n, skip):
    total = 0
    last = 1

    while total < n:
        if last != skip:
            total += last**3

        last += 1

    if total == n and last != skip and 1 != skip:
        print(n, "\tnear\t", 1, last-1, skip)

    if skip < last:
        near(n, skip+1)


def main():
    [a, b] = input("in: ").split(" ")

    a = int(a)
    b = int(b)

    for i in range(a, b+1):
        pref_normal(i)
        near(i, 1)


main()
