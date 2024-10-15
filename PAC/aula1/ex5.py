# Guardar em variaveis os diferentes valores que caracterizam o edificio
n_andares = 3
n_apartamentos_por_andar = 1
altura_andar = 3
v = 1

# Criação de uma variável para guardar a distância percorrida num dia
dist_day = 0

# Cálculo da distância percorrida num dia
# Para isso, um for loop
# Este loop vai percorrer todos os andares do edificio menos o rés-do-chão
# Logo, o range começa em 1 e vai até n_andares+1, pois a função range não inclui o último valor
for andar in range(1, n_andares+1):

    # A distância percorrida num dia é um somatorio da distância percorrida para cada andar
    # A distancia percorrida para cada andar é a altura do andar * o numero de andares * o numero de apartamentos por andar * 2 (subir e descer) * 2 (2 vezes por dia)
    dist_day += altura_andar * andar * n_apartamentos_por_andar * 2 * 2

# Multiplicar a distância percorrida num dia por 365 para obter a distância percorrida num ano
dist_year = dist_day * 365

# Imprimir a distância percorrida num ano em km (dividir por 1000)
print(dist_year/1000, "km")

# Calcular o tempo que demora a percorrer a distância percorrida num ano considerando a velocidade v
t_s = dist_year/v

# Converter o tempo de segundos para horas
t_h = t_s/3600

# Imprimir o tempo em horas
print(t_h, "h")