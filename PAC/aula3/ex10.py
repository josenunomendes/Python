def countdown(n):
    print(n)
    if n == 0:
        return 0
    countdown(n-1)

countdown(10)