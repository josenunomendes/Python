# Guardar input do utilizador relativo à largura e altura do retângulo em variáveis
width = input("width\n")
height = input("height\n")

# Esta secção do código é usada para apanhar erros.
# Por exemplo, se o utilizador inserir uma string em vez de um float, o programa iria apenas crashar
# No entanto, se usarmos try, o programa vai tentar converter o input do utilizador para um float
# No caso de não ser possível converter, o programa vai correr a secção de código dentro do except
# Neste caso, o programa vai imprimir "Error" e sair
# Se for possível converter, o programa vai continuar a correr normalmente e passar a frente o except
# Try e except ainda nao foi abordado nas aulas, portanto se se sentirem muito confusos, ignorem esta parte
try: 

    # Converter a variável para float
    width = float(width)
    height = float(height)

except ValueError:

    # Imprimir "Error" e sair
    print("Error")
    exit()

# Calcular a área do retângulo e guardar o valor na variável area
area = width*2 + height*2

# Imprimir o valor da área
print(area)