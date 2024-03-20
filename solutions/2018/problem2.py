def main():
    h1 = int(input())
    m1 = int(input())

    h2 = int(input())
    m2 = int(input())

    allm1 = h1*60+m1
    allm2 = h2*60+m2

    if allm2 > allm1:
        diff = allm2 - allm1

        print(int(diff/60), diff % 60)
    else:
        diff = ((24*60) - allm1) + allm2

        print(int(diff/60), diff % 60)


main()
