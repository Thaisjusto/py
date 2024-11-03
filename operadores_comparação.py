#operadores 
# == igual a 
# != diferente de
# > maior que
# < menor que 
# >= maior ou igual 
# <= menor ou igual 

a = b = c = False
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
x = n1 == n2
print(f'Os números digitados são iguais? {x}')

z = n1 > n2
print(f'{n1} é maior que {n2} ? {z}')

h = n1 != n2
print(f'{n1} é diferente de {n2}? {h}')
