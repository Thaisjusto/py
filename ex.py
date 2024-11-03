print('Olá, mundo!')
#---------------------------------------------------
num = input('Dgite um numero:')
print (f'o numero informado foi: {num}')
#----------------------------------------------------
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite mais um numero:'))

print(n1 + n2)
#----------------------------------------------------
medias = []

while True:
nota = float(input('digite suas notas e após, digite 0 para ter o resultado'))
if nota == 0:
       break
    medias.append(nota)
media = medias/4
print (f'Sua média é: {media}')



for x in range (1,5):
   print('Digite sua nota: ')
    nota = input()
media = nota 
    
 print(nota)


n1 = float(input('Digite a n1:'))
n2 = float(input('Digite a n2:'))
n3 = float(input('Digite a n3:'))
n4 = float(input('Digite a n4:'))

media = (n1 + n2 + n3 + n4) / 4

print (f'Sua média é: {media}')
#----------------------------------------------------

m = float(input('Digite a metragem desejada:'))

 cm = (m * 100)
print (f'{m} metros, equivale a {cm} centímetros')
#------------------------------------------------------

raio = float(input('Digite o raio do círculo:'))
area = 3.14*(raio**2)

print(f'A área deste círculo é: {area}')
#------------------------------------------------------
b = int(input('Digite o valor da base do quadrado:'))
a = int(input('Digite o valor da altura do quadrado:'))

area = b*a
dobro = area*2
print(f'A área do quadrado é igual a: {area} e o seu dobro é {dobro}')
#-------------------------------------------------------

real = float(input('Digite seu ganho por hora:'))
hora = float(input('Digite quantas horas trabalhadas:'))

salario = real * hora

print(f'Seu salário é: {salario}')
#------------------------------------------------------
