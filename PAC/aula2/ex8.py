CTP = float(input("Componente TP: "))
CP = float(input("Componente P: "))

NM = 9.5

if not (0 <= CTP <= 20 and 0 <= CP <= 20):
    print("Nota inválida")
    exit()

if CTP < NM or CP < NM:
    NF = 66

else:
    
    NF = (CTP*0.6 + CP*0.4)

if NF == 66:
    
    ATPR = float(input("Componente TPR: "))
    APR = float(input("Componente PR: "))

    if not (0 <= ATPR <= 20 and 0 <= APR <= 20):
        print("Nota inválida")
        exit()

    NF = (ATPR*0.6 + APR*0.4)

NF = int(NF+0.5)

print("Nota final: ", NF)