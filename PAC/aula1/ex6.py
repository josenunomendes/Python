# Importa o módulo math
import math

# Obter os valores dos catetos A e B
A = input("Cateto A: ")
B = input("Cateto B: ")

# Secção de código para apanhar erros semelhante aos exemplos aula0/ex6.py e aula1/ex1.py
# Em caso de duvidas consultem a descrição dos exemplos
try:

    # Converter as variáveis para float
    A = float(A)
    B = float(B)

except:

    # Imprimir "Error" e sair
    print("Error")
    exit()

# Calcular a hipotenusa do triângulo usando o teorema de Pitágoras
# O valor e guardado em C
C = math.sqrt(A**2 + B**2)

# Calcular o ângulo do triângulo no vertice adjacente ao cateto A
# Para isso é usado a função atan do módulo math, que calcula o arco tangente, em radianos, de um valor
# O valor é convertido para graus usando a função degrees do módulo math
angle = math.degrees(math.atan(B/A))

# Imprimir a hipotenusa e o ângulo
# A utilização de {:.2f} é explicada no exemplo aula0/ex7.py
print("Hipotenusa: {:.2f}".format(C))
print("Ângulo: {:.2f}".format(angle))