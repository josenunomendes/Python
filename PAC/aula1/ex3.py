# Obter o nome e o ano de nascimento do utilizador e guardar os valores em variáveis.
name = input("Como te chamas? ")
year = input("Em que ano nasceste? ")

# Secção de código para apanhar erros semelhante aos exemplos aula0/ex6.py e aula1/ex1.py
# Em caso de duvidas consultem a descrição dos exemplos
try:

    # Converter a variável para int
    year = int(year)

except:

    # Imprimir "Error" e sair
    print("Error")
    exit()

# Calcular a idade do utilizador em 2025 e guardar o valor em age
age = 2025 - year

# Imprimir o nome do utilizador e a idade que terá em 2025
# A utilização de {} e format é explicada nos exemplos aula0/ex7.py e aula1/ex1.py
print("{}, em 2025 farás {} anos".format(name, age))