### Programa para cálculo de IMC e ao final informar em qual categoria o usuário se encontra.
###Obs: Pesquisar as categorias do IMC

peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))
IMC = peso / (altura*altura)

print(f'O seu IMC é {IMC}!)