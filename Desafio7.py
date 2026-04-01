capital = float(input("Digite o capital inicial: ")) # Recebe o valor inicial 
taxa = float(input("Digite a taxa de juros (em %): ")) # Recebe a porcentagem da taxa
tempo = float(input("Digite o tempo (em meses ou anos): ")) # Recebe o período de tempo
juros = (capital * (taxa / 100) * tempo) # Calcula os juros simples usando a fórmula J = C * i * t
total = capital + juros # Calcula o montante total somando o capital original aos juros
print(f"O valor dos juros é: R${juros:.2f}") # Exibe o valor dos juros com duas casas decimais
print(f"O montante total será: R${total:.2f}") # Exibe o valor total acumulado com duas casas decimais
