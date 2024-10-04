a = 0
b = 1
c = 0
teste = [a,b]
NumeroDesejado = 20365011074
while c < NumeroDesejado:
    c = a + b
    teste.append(c)
    a = b
    b = c
if NumeroDesejado in teste:
        print(f'O numero {NumeroDesejado} está na sequencia de fibonacci')
else:
      print(f'O numero {NumeroDesejado} não foi encontrado na sequencia de fibonacci')