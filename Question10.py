### Peça 5 números e informe a soma e o maior número (OBS: sem utilizar listas)
mai = 0
soma = 0

for n in range(5):
    num = int(input('Informe o número: '))
    if num > mai:
        mai = num
    soma+=num
print(f'O maior número é {mai}!')
print(f' a soma dos números deu {soma}!')

