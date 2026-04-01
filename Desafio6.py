segundos_totais = int(input("Digite a quantidade de segundos: ")) # Recebe o total de segundos
horas = segundos_totais // 3600 # Calcula a parte inteira das horas (3600 segundos em 1 hora)
resto_segundos = segundos_totais % 3600 # Calcula o que sobrou após extrair as horas
minutos = resto_segundos // 60 # Calcula a parte inteira dos minutos do que sobrou
segundos_finais = resto_segundos % 60 # Calcula o resto final que são os segundos
print(f"{horas}h {minutos}m {segundos_finais}s") # Exibe o tempo convertido no formato h/m/s
