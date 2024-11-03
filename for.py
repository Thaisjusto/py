lista = [2,6,9,3,12,7,10]
 for item in lista:
    print(item)
 for numero in range(1,11):
     print(numero)

 for x in range(2, 20, 2):
     print(x)

pedras = ('rubi', 'esmeralda', 'quartzo', 'safira', 'diamante', 'turmalina')

for pedra in pedras:
    if pedra == 'quartzo':
        continue
    print(pedra)
