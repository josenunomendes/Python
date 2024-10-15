# Guardar input do utilizador numa variável
temp_cels = input("Temperature in Celsius: ")

# Esta secção do código é usada para apanhar erros.
# Por exemplo, se o utilizador inserir uma string em vez de um float, o programa iria apenas crashar
# No entanto, se usarmos try, o programa vai tentar converter o input do utilizador para um float
# No caso de não ser possível converter, o programa vai correr a secção de código dentro do except
# Neste caso, o programa vai imprimir "Error" e sair
# Se for possível converter, o programa vai continuar a correr normalmente e passar a frente o except
# Try e except ainda nao foi abordado nas aulas, portanto se se sentirem muito confusos, ignorem esta parte
try:

    # Converter a variável para float
    temp_cels = float(temp_cels)

except ValueError:

    # Imprimir "Error" e sair
    print("Error")
    exit()

# Converter a temperatura de Celsius para Fahrenheit
temp_fahr = (1.8 * temp_cels) + 32

# Imprimir a temperatura em Fahrenheit
# quando utilizamos "{}" dentro de uma string, estamos a criar um placeholder
# Assim, com o metodo format, podemos substituir o placeholder pelo valor da variável,
# A parte :.2f significa que o valor sera formatado com 2 casas decimais em float
print("{:.2f} ºC = {:.2f} ºF".format(temp_cels, temp_fahr))