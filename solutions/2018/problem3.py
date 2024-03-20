def eq(a, b):
    return "".join(a).lower() == "".join(reversed(b)).lower()


def palendrome(s):
    halfway = int(len(s)/2)
    top = [s[a] for a in range(halfway)]
    bottom = [s[a] for a in range(halfway + (len(s) % 2), len(s))]

    return eq(top, bottom)


def main():
    s = list(input())

    longestl = 0
    longests = []

    for i in range(len(s)):
        for j in range(i, len(s)):
            l = j-i
            sub = [s[a] for a in range(i, j+1)]

            if palendrome(sub):
                if (longestl < l):
                    longestl = l
                    longests = sub
                elif (longestl == l and str(sub) > str(longests)):
                    longestl = l
                    longests = sub

    if longestl == 0:
        print(sorted(s)[0])
    else:
        print("".join(longests))

    pass


main()
