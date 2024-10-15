# Guardar input do utilizador numa variável
temp_cels = input("Temperature in Celsius: ")

# Converter a variável para float
# Se não for possível converter, imprimir "Error" e sair
# Desta forma, o programa fica com erro
try:
    temp_cels = float(temp_cels)

except ValueError:
    print("Error")
    exit()

# Converter a temperatura de Celsius para Fahrenheit
temp_fahr = (1.8 * temp_cels) + 32

# Imprimir a temperatura em Fahrenheit
# quando utilizamos "{}" dentro de uma string, estamos a criar um placeholder
# Assim, com o metodo format, podemos substituir o placeholder pelo valor da variável,
# A parte :.2f significa que o valor sera formatado com 2 casas decimais em float
print("{:.2f} ºC = {:.2f} ºF".format(temp_cels, temp_fahr))