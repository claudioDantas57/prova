###Faça um programa que pergunte o ano de nascimento do usuário e responde quantos anos ela terá ao final de 2022.

anoNasc = anoAtual = idade =0

anoAtual = int(input('Em que ano estamos?: '))
anoNasc = int(input('Quando você nasceu?: '))
idade = anoAtual - anoNasc

print(f'Você tem  {idade} anos"')
