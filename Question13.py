### Pedir 10 números, se o número for par, vai para uma lista, se for impar, vai para outra lista. Ao final,
# mostrar as duas listas, a soma dos pares, a soma dos impares e a soma das duas listas
pares = []
impares = []

for _ in range(10):
    listNum = int(input('Digite um número:'))

    if listNum % 2 ==0:
        pares.append(listNum)
    else:
        impares.append(listNum)



print(f'A lista dos números pares é{pares}!')
print(f'A lista dos números ímpares é{impares}!')
sompares = sum(pares)
somaimares = sum(impares)
print(f'A soma dos pares é {sompares} e a soma dos ímpares é {somaimares}!')
print(f'A soma dos pares e ímpares é {sompares+somaimares}!')