### 07. Faça um programa que pergunta a temperatura em graus Celsius e responde a temperatura correspondente em graus Fahrenheit.
### 07.1 Faça um programa que pergunta a temperatura em graus Fahrenheit e responde a temperatura correspondente em graus Celsius.
###(0 °C × 9/5) + 32 = 32 °F    TC/5 = (TF – 32)/9,    F: 40/5 = (TF – 32)/9.

CelFahr = int(input('Qual a temperatura em graus célsius? : '))
FahrCel = int(input('Qual a temperatura em graus Fahrenheit?: '))

CF = ((CelFahr*9)/5) + 32
FC = (FahrCel - 32) / 9
print(f'A temperatura de {CelFahr}º é {FahrCel}º')
print(f'A temperatura em {FahrCel}º é {CelFahr}º')