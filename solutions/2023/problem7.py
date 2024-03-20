class Board:
    pegs: list[list[bool]] = []
    history: list[tuple[int,int]] = []

    def with_items(pegs: list[list[bool]], hist: list[tuple[int,int]]):
        this = Board([])
        this.pegs = pegs
        this.history = hist

        return this

    def __init__(self, filled: list[int]):
        filled = [f-1 for f in filled]

        self.pegs = [[False for _ in range(row)] for row in range(1,7)]

        for f in filled:
            i = 0
            while i < f:
                i += 1
                f -= i

            self.pegs[i][f] = True

    def at(self, row: int, col: int):
        if row >= len(self.pegs) or row < 0:
            return None
        
        if col >= len(self.pegs[row]) or col < 0:
            return None
        
        return self.pegs[row][col]

    def at_or_false(self, row: int, col: int):
        a = self.at(row,col)

        if a == None:
            return False
        
        return a

    def tat(self, rc: tuple[int,int]):
        row,col = rc

        return self.at(row,col)

    def set(self, rc: tuple[int,int], val:bool):
        row,col = rc

        self.pegs[row][col] = val

    def tat_or_false(self, rc: tuple[int,int]):
        row,col = rc
        
        return self.at_or_false(row,col)

    def clone(self):
        pegs = [[item for item in row] for row in self.pegs]
        hist = [(k,v) for k,v in self.history]

        return Board.with_items(pegs,hist)

    def moves_from(self, row: int, col: int) -> list[tuple[tuple[int,int], tuple[int,int], tuple[int,int]]]:
        directions: list[tuple[int,int]] = [
            (1, 1),
            (1, 0),
            (-1, -1),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = []

        for ro, co in directions:
            rowtaken = row+ro
            coltaken = col+co

            rowjump = rowtaken+ro
            coljump = coltaken+co

            if self.at_or_false(rowtaken, coltaken) and self.at_or_false(rowjump, coljump):
                moves.append(((row, col), (rowtaken, coltaken), (rowjump, coljump)))

        return moves

    def possible_moves(self) -> list[tuple[tuple[int,int], tuple[int,int], tuple[int,int]]]:
        empty: list[tuple[int,int]] = []

        for row in range(len(self.pegs)):
            for col in range(len(self.pegs[row])):
                if not self.pegs[row][col]:
                    empty.append((row, col))

        moves = []

        for row,col in empty:
            moves.extend(self.moves_from(row,col))

        return moves
    
    def map_tuple(sq: tuple[int,int]) -> int:
        row, col = sq
        total = 0

        for i in range(1,7):
            if row == 0:
                break

            row -= 1
            total += i

        return total+col+1
    
    def map_move(move: tuple[tuple[int,int], tuple[int,int], tuple[int,int]]) -> tuple[int,int]:
        target, _, start = move

        return [Board.map_tuple(start), Board.map_tuple(target)]

    def make(self, move: tuple[tuple[int,int], tuple[int,int], tuple[int,int]]):
        self.history.append(Board.map_move(move))

        to, taken, jumper = move

        self.set(to, True)
        self.set(taken, False)
        self.set(jumper, False)

    def make_all(self):
        boards: list[Board] = []

        for move in self.possible_moves():
            cloned:Board = self.clone()
            cloned.make(move)
            boards.append(cloned)

        return boards
    
    def printhist(self):
        print(len(self.history))
        for s,e in self.history:
            print(f"{s}-{e}")

def least(without: list[Board]) -> Board | None:
    if len(without) == 0:
        return None
    
    l = without[0]

    for item in without:
        smaller = False

        for orig, new in zip(l.history, item.history):
            borig, eorig = orig
            bnew, enew = new

            if bnew < borig or (bnew == borig and enew < eorig):
                smaller = True
                break

            if bnew == borig and enew == eorig:
                continue

            break

        if smaller:
            l = item

    return l

def flatten(l: list[list[Board]]) -> list[Board]:
    return [item for row in l for item in row]

def main():
    pegs = [int(i) for i in input().split()]
    pegs = pegs[1:] # first number is just the number of inputs

    positions: list[Board] = [Board(pegs)]

    while True:
        without = [p for p in positions if len(p.possible_moves()) == 0]
        smallest = least(without)

        if smallest is not None:
            smallest.printhist()
            break

        newpos = flatten(map(lambda p: p.make_all(), positions))
        positions = newpos

main()