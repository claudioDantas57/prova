### Crie um algoritmo que informe o tipo de um valor informado pelo usuário



v = input('Informe um valor: ')
print(type(v))

if v == str:
    print(f'O valor é uma string!')
elif v == int:
    print(f'O valor é um número inteiro!')
elif v == float:
    print(f'O valor é um número float!')
else:
    print(f"O valor é booleano!")

