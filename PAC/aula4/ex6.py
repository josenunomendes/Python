def leibnizPi4(n):
    pi = 1

    for i in range(1, n):
        pi += (-1)**i/(2*i + 1)

    return pi*4

print(leibnizPi4(1000000))