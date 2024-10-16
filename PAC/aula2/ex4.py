price = 1.4
discount = 0.10

liters = float(input("Quantos litros de gasolina deseja abastecer? "))

if liters <= 40 and liters >= 0:
    total = price * liters

elif liters > 40:
    total = price * liters * (1 - discount)

else:
    print("Valor inválido")
    exit()

print("Total a pagar: {:.2f}".format(total))