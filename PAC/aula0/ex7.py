# A edição do ficheiro welcome.py foi realizada neste ficheiro, ex7.py, e não no ficheiro original.

# Mensagem do exercício
message = """
Caro/a {},

Bem-vindo/a à disciplina de Fundamentos de Programação
e ao curso de {}.

Esperamos que aprendas muito e que te divirtas.

Cumprimentos,

Os Profes de FP.
"""
# Pedir ao utilizador o seu nome e curso e guardar nas respetivas variáveis
name = input("Como te chamas? ")
course = input("Qual é o teu curso? ")

# Imprimir a mensagem de boas-vindas
# Usamos as {} como placeholders na string
# Usando o metodo format, podemos substituir os placeholders pelos valores das variáveis
print(message.format(name, course))