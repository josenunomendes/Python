# Guardar o valor das horas e minutos iniciais nas variaveis hi e mi
hi = 6
mi = 52

# Calcular o numero total de minutos da hora inicial
mi_total = hi * 60 + mi

# Calcular o numero total de minutos da hora de chegada
# Assim, soma-se ao numero total de minutos da hora inicial o tempo que demorou a ir e voltar
# Na ida, percorreu-se 1 km a 10 min/km na primeira parte e 3 km a 6 min/km na segunda parte
# Na volta, percorreu-se o mesmo caminho, logo, 1+3 km a passo de 10 min/km
mf_total = mi_total + 1*10 + 3*6 + 4*10

# Calcular a hora final em horas e minutos
# Para isso divide-se o numero total de minutos por 60 e guarda-se o quociente nas horas e o resto nos minutos
hf = mf_total // 60
mf = mf_total % 60

# Imprimir a hora final
print("A hora final é: {}:{:02d}".format(hf, mf))
