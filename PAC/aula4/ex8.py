def fib(n):
    
    if n == 0:
        return 0

    if n == 1:
        return 1
    
    sumprev = 0
    sumcur = 1
    print(sumprev)
    print(sumcur)

    for i in range(2, n):
        sumcurtemp = sumcur
        sumcur = sumcur + sumprev
        sumprev = sumcurtemp
        print(sumcur)

fib(10)