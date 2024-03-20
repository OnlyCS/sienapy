import threading


def largest_ladder(board):
    llen = 0
    istart = 0

    for i in range(len(board)):
        if (board[i] - i) > llen and board[i] < len(board):
            llen = board[i] - i
            istart = i

    return istart


def belowllstart(board):
    l = largest_ladder(board)

    return board[:l]


def abovellend(board):
    l = largest_ladder(board)
    e = board[l]

    return board[e:]


def split(board):
    return [belowllstart(board), abovellend(board)]


def find_path(board):
    largest = largest_ladder(board)

    if largest == 0:
        return []

    paths = [[largest]]

    [below, above] = split(board)

    if below != []:
        paths.insert(0, find_path(below))

    if above != []:
        paths.append(find_path(above))

    # flatten
    return [item for sublist in paths for item in sublist]


alllowest = 100000


def togoal(board, at, goal, currdep, maxdep):
    global alllowest

    if at == goal:
        return currdep

    if currdep >= maxdep:
        return -1

    lowest = 100000

    def f(roll):
        global alllowest
        nonlocal lowest

        if currdep > alllowest or currdep > lowest:
            return

        if (at+roll) >= len(board):
            return

        i = -1

        if at+roll == goal:
            i = togoal(board, at+roll, goal, currdep+1,
                       min(maxdep, alllowest, lowest))
        else:
            i = togoal(board, board[at+roll], goal,
                       currdep+1, min(maxdep, lowest, alllowest, lowest))

        if lowest > i and i != -1:
            if currdep == 0:
                alllowest = i

            lowest = i

    threads = []

    for roll in range(1, 7):
        threads.append(threading.Thread(f(roll)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return lowest


def main():
    global alllowest

    [lenb, isnakes, iladders] = [int(x) for x in input().split()]
    board = [int(x) for x in range(lenb)]

    for _ in range(isnakes):
        [start, end] = [int(x)-1 for x in input().split()]
        board[start] = end

    for _ in range(iladders):
        [start, end] = [int(x)-1 for x in input().split()]
        board[start] = end

    path = find_path(board)

    path.append(len(board) - 1)

    total = 0
    at = -1

    for p in path:
        alllowest = 100000

        total += togoal(board, at, p, 0, ((p-at)/4)+4)
        at = board[p]

    if total > 100000:
        print("NOT POSSIBLE")

    print(total)


main()
