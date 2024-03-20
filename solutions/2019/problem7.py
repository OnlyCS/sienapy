parsedict: dict[str,bool|None] = {
    "O": None,
    "W": False,
    "B": True
}

revdict = {v:k for k,v in parsedict.items()}

class Board:
    board: list[list[bool|None]]

    def __init__(self, parse: list[str]):
        parse: list[list[str]] = [list(s) for s in parse]

        for i in range(len(parse)):
            for j in range(len(parse[i])):
                parse[i][j] = parsedict[parse[i][j]]

        self.board = parse

    def rowsumeq(self, i:int):
        row = self.board[i]

        off = 0
        on = 0
        unk = 0

        for item in row:
            if item == None: unk += 1
            elif item: on += 1
            else: off += 1

        if unk == 0: return

        if off == len(row) / 2:
            for i in range(len(row)):
                if row[i] == None:
                    row[i] = True

        if on == len(row) / 2:
            for i in range(len(row)):
                if row[i] == None:
                    row[i] = False

    def colsumeq(self, i:int):
        col = [row[i] for row in self.board]

        off = 0
        on = 0
        unk = 0

        for item in col:
            if item == None: unk += 1
            elif item: on += 1
            else: off += 1

        if unk == 0: return

        if off == len(col) / 2:
            for j in range(len(col)):
                if col[j] == None:
                    self.board[j][i] = True

        if on == len(col) / 2:
            for j in range(len(col)):
                if col[j] == None:
                    self.board[j][i] = False

    def rowthree(self, i:int):
        row = self.board[i]

        for j in range(len(row)-2):
            first = row[j]
            second = row[j+1]
            third = row[j+2]

            if first == second and third == None and first != None:
                row[j+2] = not first
            elif second == third and first == None and second != None:
                row[j] = not second
            elif first == third and second == None and first != None:
                row[j+1] = not first

    def colthree(self, i:int):
        col = [row[i] for row in self.board]

        for j in range(len(col)-2):
            first = col[j]
            second = col[j+1]
            third = col[j+2]

            if first == second and third == None and first != None:
                self.board[j+2][i] = not first
            elif second == third and first == None and second != None:
                self.board[j][i] = not second
            elif first == third and second == None and first != None:
                self.board[j+1][i] = not first

    def solverow(self, i:int):
        self.rowsumeq(i)
        self.rowthree(i)

    def solvecol(self, i:int):
        self.colsumeq(i)
        self.colthree(i)

    def solve(self, i:int):
        self.solverow(i)
        self.solvecol(i)
    
    def fullstep(self):
        for i in range(len(self.board)):
            self.solve(i)

    def solved(self):
        flattened = [item for row in self.board for item in row]
        nones = [item for item in flattened if item == None]

        if len(nones) == 0:
            return True
    
        return False
    
    def print(self):
        for row in self.board:
            strs = [revdict[i] for i in row]
            print("".join(strs))
    
def main():
    num = int(input())
    strs = [input() for _ in range(num)]

    board = Board(strs)

    while not board.solved():
        board.fullstep()

    board.print()

main()