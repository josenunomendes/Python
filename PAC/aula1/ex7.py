# This program reads the coordinates of two points (x1,y1) and (x2,y2).
# Guarda as coordenadas dos pontos (x1,y1) e (x2,y2)
x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

# Find and print the distance between the points!
# Calcula a distância no eixo dos x e no eixo dos y
dx = x2 - x1
dy = y2 - y1

# Calcula a distância entre os dois pontos usando o teorema de Pitágoras
# É de notar que a raiz quadrada é calculada usando **0.5
d = (dx**2 + dy**2)**0.5

# Imprime a distância
# A utilização de {:.2f} é explicada no exemplo aula0/ex7.py
print("Distance: {:.2f}".format(d))