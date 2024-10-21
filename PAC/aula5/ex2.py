def inputFloatList():
    print("Lista de números reais:")
    lst = []

    while True:
        n = input()
        if n == "":
            print(lst)
            return lst
        
        lst.append(float(n))

def countLower(lst, v):
    count = 0
    for i in lst:
        if i < v:
            count += 1
    return count

def minMax(lst):
    lmin = lst[0]
    lmax = lst[0]

    for i in lst:
        if i < lmin:
            lmin = i
        elif i > lmax:
            lmax = i
    
    return lmin, lmax


lst = inputFloatList()
avg = sum(lst) / len(lst)
v = countLower(lst, avg)
lmin, lmax = minMax(lst)

print(f"Lista: {lst}")
print(f"Média: {avg}")
print(f"Quantidade de números menores que a média: {v}")
print(f"Mínimo: {lmin}")
print(f"Máximo: {lmax}")