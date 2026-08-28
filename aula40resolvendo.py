#67. Exercício guiado - Calculadora - Parte 1
'''
pedir o primeiro numero
segundo numero
operador ( +, -, //, *)


.lower() = sair sempre com letra minuscula
startswith('letra') = começar com tal letra
endswith('letra') = termina com tal letra
''' 



''' 
calculadora_on = True
while calculadora_on:

    primeiro_numero = int(input('Qual o primeiro numero? '))
    segundo_numero = int(input('Qual o segundo numero? '))
    print('1[adição]')
    print('2[subtrição]')
    print('3[multiplicação]')
    print('4[divisão]')
    operador = int(input('Qual operador vai ser usado? ')) 

    try:
        num_1_float = float(primeiro_numero)
        num_2_float = float(segundo_numero)
'''        
''' 
if operador == 1:
    conta = primeiro_numero + segundo_numero
    print(f'resultado: {conta}')   
elif operador == 2:
    conta = primeiro_numero - segundo_numero
    print(f'resultado: {conta}')   
elif operador == 3:
    conta = primeiro_numero * segundo_numero
    print(f'resultado: {conta}')   
elif operador == 4:
    conta = primeiro_numero / segundo_numero
    print(f'resultado: {conta}')    
'''
'''  
  except:
        print(error)

    sair = input('Quer sair? [s]im:').lower().startswith('s') 
    
    if sair is True:
        break
''' 
