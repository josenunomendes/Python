# Guardar os valores de v1 e v2 em variáveis
v1 = 10
v2 = 20

# Deduzir a fórmula para calcular a velocidade média
# v1 = d/t1
# v2 = d/t2
# v1*t1 = v2*t2
# t(total) = t1+t2
# t(total) = d/v1 + d/v2
# vm = d/t(total)
# vm = d/(d/v1 + d/v2)
# vm = d/(d*(1/v1 + 1/v2))
# vm = 1/(1/v1 + 1/v2)
# vm = 1/((v1+v2)/(v1*v2))
# vm = v1*v2/(v1+v2)

# Aplicar a fórmula e guardar o resultado em vm
vm = (v1*v2)/(v1+v2)

# Imprimir o resultado
print(vm)