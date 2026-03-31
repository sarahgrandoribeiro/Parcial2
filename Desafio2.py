# Pedir um número inteiro e guardar na variável n 
n = int(input('Diga um número inteiro:'))
# Utilizando % para ver se o resto da divisão do número por 2 é 0 
if n % 2 == 0:
# Caso o resto realmente for 0, o número é par
    print('O número é par')
# Caso o resto for diferente de 0 o número é impar 
else:
# mostre que o número é impar
    print('o número é ímpar')
