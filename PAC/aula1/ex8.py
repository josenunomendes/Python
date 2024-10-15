# Guardar os valores do exercicio nas respectivas variaveis
PF = 20
PC = 24.95
IMP = 0.23
SPA = 0.2

# Calculo do lucro por livro
# PC  = (PF + L) * (1 + IMP) + SPA
# PC - SPA = (PF + L) * (1 + IMP)
# (PC - SPA) / (1 + IMP) = PF + L
# ((PC - SPA) / (1 + IMP)) - PF = L
L = ((PC - SPA) / (1 + IMP)) - PF

# Calculo do lucro total
LT = L * 500

# Mostrar o lucro total
print("O lucro é de: {:.2f} euros".format(LT))

# Calculo do valor de impostos coletados
# Dado que os impostos são aplicados antes do SPA, apenas o preço de fabrico e lucro são taxados
taxas_coletadas = (PF + L) * 500 * IMP

# Mostrar o valor de impostos coletados
print("O valor de impostos coletados é de: {:.2f} euros".format(taxas_coletadas))

# Calculo do valor total de SPA coletado
# O SPA é um valor fixo por livro
SPA_total = SPA * 500

# Mostrar o valor total de SPA coletado
print("O valor total de SPA coletado é de: {:.2f} euros".format(SPA_total))