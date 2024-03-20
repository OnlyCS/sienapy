def main():
    s = list(input())
    ni = int(input())
    i = [int(input()) for _ in range(ni)]
    i = sorted(i)

    for j in reversed(i):
        s.pop(j-1)

    print("".join(s))


main()
