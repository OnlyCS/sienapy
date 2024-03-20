def main():
    a = input("list one: ").split(" ")[:-1]
    b = input("list two: ").split(" ")[:-1]

    for _ in range(1, len(b)):
        t = b[0]
        b = b[1:]
        b.append(t)

        if b == a:
            print("CYCLE")
            return

    print("NOCYCLE")


main()
