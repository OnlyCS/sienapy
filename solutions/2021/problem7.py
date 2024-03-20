from math import floor, ceil, lcm, gcd

def fracsub(den1: int, den2: int) -> int:
    # 1/den1 - 1/den2
    # find lcm
    
    den = lcm(den1, den2)
    
    n1 = int(den/den1)
    n2 = int(den/den2)
    
    # n1/den - n2/den == (n1-n2)/den
    nsum = n1 - n2

    greatest = gcd(nsum, den)
    nsum /= greatest
    den /= greatest

    if nsum != 1:
        print("It was at this point he realized")
        raise Exception(f"He died {den1}, {den2}, {den}, {nsum}")
    
    return int(den)

# 1, 1 ==> 1/1
# 2, 1 ==> 1/2
def at(row: int, col: int) -> int:
    if col == row or col == 1:
        return row
    
    if col == 2 or col == row-1:
        return row*(row-1)
    
    if row % 2 == 0 and (col == row/2 or col == (row/2)+1):
        lastrow = row - 1
        halfway = row / 2
        last = at(lastrow, halfway)
        half = int(last/2)
        
        return half

    signum = col > row/2

    match (signum):
        case True: signum = 1
        case False: signum = -1

    rootrow = row-1
    rootcol = col+min(signum,0)
    root = at(rootrow, rootcol)

    subrow = row
    subcol = col+signum
    sub = at(subrow, subcol)
    
    return fracsub(root, sub)

def main():
    [a,b] = [int(i.strip()) for i in input().split() if not (i.isspace() or i == "")]

    print(f"1/{at(a,b)}")

main()