palavra = 'pneumoultrAmicroscopicocillicovulcanoconiotico'
contagem = 0
for letra in palavra:
    if letra.lower() == "a":
        contagem += 1
print(f'Foram encontradas {contagem} letras "a" na palavra')