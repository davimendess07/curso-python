#50. Introdução ao try e except para capturar erros(exceptions)

'''
Introdução ao try/except

try --> tentar executar o código

except --> ocorreu algum erro ao tentar executar
'''

numero_str = input(
    'Vou dobrar o número que vc digitar: '
    )

try:
    numero_float = float(numero_str) #fail fast, errar o mais rapido possivel e ir pra execeção
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}') 
except:
    print('isso não é um número')

# if (numero_str.isdigit()):
#     numero_float = float(numero_str) 
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')#converter a string para numero com ponto flutuante

# else:
#     print('isso não é um número')


#try - tentar executar o codigo q estiver nele, consegue capturar o erro
#except- se ocorrer algum erro dentro do try, pula pro except 