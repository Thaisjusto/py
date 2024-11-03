n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))

media = (n1 + n2) / 2 

if media >= 7:
    print('Aprovado!')
elif media >= 5:
   print('Você esta em recuperação :(')
else:
   print('Reprovado! Até ano que vem otário hihihi')

