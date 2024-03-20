from itertools import permutations
from typing import Callable

dshape = {
    "d": 0,
    "p": 1,
    "o": 2
}

dcolor = {
    "g": 0,
    "v": 1,
    "r": 2
}

dfill = {
    "h": 0,
    "l": 1,
    "s": 2,
}

rdshape = {v:k for k,v in dshape.items()}
rdcolor = {v:k for k,v in dcolor.items()}
rdfill = {v:k for k,v in dfill.items()}

class Card:
    shape: int # 0 - diamond, 1 - squiggle, 2 - oval
    fill: int # 0 - hollow, 1 - striped, 2 - solid
    count: int # 1, 2, or 3
    color: int # 0-green, 1-purple, 3-red

    def __init__(self, shape, fill, count, color):
        self.shape = shape
        self.fill = fill
        self.count = count
        self.color = color

    def parse(s: str):
        ct = int(s[0])
        shape = s[1]
        fill = s[2]
        color = s[3]

        fill = dfill[fill.lower()]
        shape = dshape[shape.lower()]
        color = dcolor[color.lower()]

        return Card(shape, fill, ct, color)
    
    def __str__(self) -> str:
        s = rdshape[self.shape]
        ct = str(self.count)
        f = rdfill[self.fill]
        c = rdcolor[self.color]

        return (ct + s + f + c).upper()
    
    def __eq__(self, other: object) -> bool:
        self.shape == other.shape and self.color == other.color and self.count == other.count and self.fill == other.fill

    def __hash__(self) -> int:
        tup = self.shape, self.color, self.count, self.fill
        return tup.__hash__()

def checkeq(cards: list[Card], prop: Callable[[Card], int]):
    [c1,c2,c3] = map(prop, cards)

    return c1 == c2 and c2 == c3

def checkneq(cards: list[Card], prop: Callable[[Card], int]):
    [c1,c2,c3] = map(prop, cards)

    ck0 = c1 != c2
    ck1 = c1 != c3
    ck2 = c2 != c3

    return ck0 and ck1 and ck2

def check(cards: list[Card], prop: Callable[[Card], int]):
    return checkeq(cards,prop) or checkneq(cards,prop)

def shape(cards: list[Card]):
    return check(cards, lambda c: c.shape) 

def col(cards: list[Card]):
    return check(cards, lambda c: c.color) 

def fill(cards: list[Card]):
    return check(cards, lambda c: c.fill)

def count(cards: list[Card]):
    return check(cards, lambda c: c.count) 

def filt(cards: list[Card]):
    return count(cards) and fill(cards) and col(cards) and shape(cards)

def filterperms(cards: list[Card]) -> set[Card]:
    perms = list(permutations(cards, 3))
    perms = filter(filt, perms)
    return [frozenset(i) for i in perms]

def order(cards: list[frozenset[Card]]):
    cards = [sorted(list(perm), key=lambda c: str(c)) for perm in cards]
    cards = sorted(cards, key=lambda cds: "".join([str(c) for c in cds]))

    return cards

def main():
    ct = int(input())
    p = []
    for c in range(ct):
        p.append(Card.parse(input()))

    d = False
    for n in order(dict.fromkeys(filterperms(p)).keys()):
        for k in n:
            print(str(k), end=" ")
        print("")
        d = True

    if not d:
        print("NO SETS")

main()