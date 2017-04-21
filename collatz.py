def collatz(n):
    hist=[n]
    res=n
    while res <> 1:
        if res % 2 == 0:
            res=res/2
        else:
            res=res*3+1
        hist.append(res)
    return hist

