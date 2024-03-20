def openloop(arr, opennum, ctr, vstart):
    i = int(arr[opennum])

    if i == vstart:
        return ctr

    return openloop(arr, i, ctr + 1, vstart)


def main():
    input("num inputs: ")
    jerseys = [int(i) - 1 for i in input("inputs: ").split(" ")]

    greatest = 0
    least = 99999

    for i in range(0, len(jerseys)):
        n = openloop(jerseys, jerseys[i], 1, jerseys[i])

        if greatest < n:
            greatest = n

        if least > n:
            least = n

    print(greatest, least)


main()
