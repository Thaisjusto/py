# for cont_ex in range (1,6): #nos parenteses esta a contagem
#     print(f'\nRodada: {cont_ex}') #\n para qubrar uma linha
#     for cont_in in range (5, 0, -1): #-1 esta fazendo um decremento
#         print(f'Valor: {cont_in}')

# print('fim dos laços')

import random

for A in range (1,6):
    print(f'\nConjunto {A}')
    for B in range (5):
        num = random.randint(1,100)
        print(f'Valor: {num}')