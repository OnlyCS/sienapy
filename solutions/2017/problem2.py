def allsq(m: int, n: int) -> int:
    return sum([((m-k)*(n-k)) for k in range(0, m)])


def main():
    m = int(input("m: "))
    n = int(input("n: "))
    print(allsq(m, n))


main()
