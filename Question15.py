### Solicite a idade de 5 pessoas e ao final conte quantas pessoas são maiores de idade,
# a soma de todas as idades, a média das idades, o valor máximo, o valor mínimo, ordene de forma crescente e decrescente.
listaidade= []
maiorIdade = []


for i in range (5):
    idade = int(input('Qual sua idade?: '))
    if idade>=18:
        maiorIdade.append(idade)
    listaidade.append(idade)

somaIdade = sum(listaidade)
mediaIdade = sum(listaidade)/len(listaidade)
maisVelho = max(listaidade)
maisJovem = min(listaidade)

print(f'A quantide de pessoas maiores de 18 anos é {maiorIdade} ')
print(f'A soma de todas as idades é{somaIdade}')
print(f'A média das idade é {mediaIdade}')
print(f'A pessoa mais velha tem {maisVelho} anos')
print(f'A pessoa mais jóvem tem {maisJovem} anos')
listaidade.sort()
print(f'A ordem crescente das idades é; {listaidade}')
listaidade.reverse()
print(f'A lista das idades em ordem decrescente é {listaidade}')
