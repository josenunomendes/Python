count = 1
seqmax = float(input("Enter a sequence of numbers\n"))
seqmin = seqmax

while True:

    seq = input()

    if seq == "":
        break

    count += 1
    seqmax = max([float(seq), seqmax])
    seqmin = min([float(seq), seqmin])

print("The sequence had", count, "numbers and the maximum was", seqmax, "and the minimum was", seqmin)