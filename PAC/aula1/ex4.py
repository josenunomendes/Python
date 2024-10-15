# Obter o input do utilizador em segundos e guarda na variável sec
sec = input("Segundos: ")

# Secção de código para apanhar erros semelhante aos exemplos aula0/ex6.py e aula1/ex1.py
# Em caso de duvidas consultem a descrição dos exemplos
try:

    # Converter a variável para int
    sec = int(sec)

except:

    print("Error")
    exit()

# Calculo do número de horas
# Para isso é usado o operador // que calcula a divisão inteira
# Assim, dado que existem 3600 segundos numa hora, o número de horas é sec//3600
# O resto da divisão deverá ser representado em minutos e/ou segundos
h = sec//3600

# Calculo do número de minutos
# O operador % calcula o resto da divisão, dando-nos o número de segundos que não foram contabilizados nas horas
# Da mesma forma que no passo anterios, existem 60 segundos num minuto, portanto o número de minutos é (sec%3600)//60
m = (sec%3600)//60

# Calculo do número de segundos
# O numero de segundos é o resto das divisões anteriores
s = (sec%3600)%60

# Imprimir o resultado
# A utilização de {} e format é explicada nos exemplos aula0/ex7.py e aula1/ex1.py
print("{:02d}:{:02d}:{:02d}".format(h, m, s))