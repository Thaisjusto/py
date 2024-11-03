# num = 1
# while num <= 10:
#     print(num)
#     num += 1 #incrementando a variavel para que o loop não seja infinito

nome = None #none para criar uma variavel vazia
while True:
    print('Digite seu nome ou x para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem vindo, {nome}')
print('Até logo!')