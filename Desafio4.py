n1 = float(input("Digite o primeiro número: ")) # Recebe o primeiro operandor
n2 = float(input("Digite o segundo número: ")) # Recebe o segundo operandor
op = input("Digite a operação (+, -, *, /): ") # Recebe o símbolo da operação 
if op == '+': # Verifica se a operação é soma
    print(f"Resultado: {n1 + n2}") # Exibe a soma
elif op == '-': # Verifica se a operação é subtração
    print(f"Resultado: {n1 - n2}") # Exibe a subtração
elif op == '*': # Verifica se a operação é multiplicação
    print(f"Resultado: {n1 * n2}") # Exibe a multiplicação
elif op == '/' and n2 != 0: # Verifica se é divisão e se o divisor não é zero
    print(f"Resultado: {n1 / n2}") # Exibe a divisão
else: # Caso a operação seja inválida ou divisão por zero
    print("Operação inválida ou erro de divisão.") # Exibe mensagem de erro
