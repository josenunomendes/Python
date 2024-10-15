# Try running this program.
# Then change it to generate another subplot with the product of y1 and y2.

# Esta secção importa as bibliotecas necessárias para a execução do programa
import numpy as np
import matplotlib.pyplot as plt

# Segundo a deocumentação, o método figure cria uma nova figura sem a desenhar na tela
plt.figure(1)

# Segundo a documentação, o método arange cria um conjunto com valores de 0 a 5 com um incremento de 0.1
# Esse conjunto é guardado na variável t
t = np.arange(0.0, 5.0, 0.1)  # try printing t

# Segundo a documentação, o método subplot cria um novo grafico, ou plot, na figura
plt.subplot(2, 1, 1)

# Segundo a documentação, o método exp calcula o exponencial do valor/valores fornecidos
# Neste caso, o exponencial dos valores de t
# O resultado é guardado na variável y1
# Desta maneira, cria-se um conjunto de pontos com pequenos intervalos que pertencem a função matemática y = e^-t
y1 = np.exp(-t)

# Segundo a documentação, o método plot desenha um gráfico com os valores fornecidos
# Assim, desenha-se um gráfico com pontos de t no eixo x e y1 no eixo y
# O valor da string é usado para definir a cor e o tipo de linha, sendo neste caso azul
plt.plot(t, y1, 'b')  # try 'g' or 'bo' or 'k+'

# Esta secção realiza o mesmo que a secção anterior, mas com uma função diferente
plt.subplot(2, 1, 2)
y2 = np.cos(2*np.pi*t)

# A string 'ro-' define um grafico com pontos vermelhos e linhas
plt.plot(t, y2, 'ro-')

# O método show mostra os gráficos criados na tela
plt.show()