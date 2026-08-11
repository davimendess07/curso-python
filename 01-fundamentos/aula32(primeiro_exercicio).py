
print ('Faça um programa que peça ao usuário para digitar um número inteiro,\
informe se este número é par ou ímpar. Caso o usuário não digite um número\
inteiro, informe que não é um número inteiro..')
print('')
print('')
print('')

numero = (input('digite um número inteiro: '))
try:
    numero_int = int(numero)
    if (numero_int % 2 == 0):
        print(f'{numero} este numero é par')
    else:
        print(f'{numero} este numero é impar')
except:
    print('isso não é um número inteiro...')


