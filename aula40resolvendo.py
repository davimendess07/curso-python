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
    try:
        primeiro_numero = float(input('Qual o primeiro numero? '))
        segundo_numero = float(input('Qual o segundo numero? '))
        print('1[adição]')
        print('2[subtrição]')
        print('3[multiplicação]')
        print('4[divisão]')
        operador = int(input('Qual operador vai ser usado? ')) 

        if operador < 1 or operador > 4:
           print('Escolha os operadores da tabela!')

        elif operador == 1:
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
    
    except:
        print('Escolha os operadores da tabela!')
            

    sair = input('Quer sair? [s]im:').lower().startswith('s')
    if sair is True:
        break
''' 
'''
anotações:
 outro modo de usar o except é o except Exception as (e a variavel que vc quer tratar o erro):
 Flags
 Continue, quebra e volta para o começo - Útil quando detecta um problema e não faz 
 sentido continuar aquela volta.

CODIGO DO PROFESSOR QUE FIZ JUNTO DEPOIS DO MEU:
'''   
calculadora_on = True
while calculadora_on:
    primeiro_numero = input('Qual o primeiro numero? ')
    segundo_numero = input('Qual o segundo numero? ')
    operador = input('Qual operador vai ser usado? (+-/*) ')


    primeiro_numero_float = 0
    segundo_numero_float = 0
    numero_validos = None    #Flags
    try: 
        primeiro_numero_float = float(primeiro_numero)
        segundo_numero_float = float(segundo_numero)
        numero_validos = True
       

    except:
        numero_validos = None

    if numero_validos is None:
        print('Um ou os dois numeros são invalidos.')
        continue #devolve para o topo do laço

    operadores_permitidos = '+=/*'

    if operador not in operadores_permitidos:
        print('operador invalido')


    if len(operador) > 1:
        print('digite apenas um operador')
        continue 

    print('Realizando sua conta. Confira o Resultado abaixo! ')
    if operador == '+':
        conta = primeiro_numero_float + segundo_numero_float
        print(f'RESULTADO : {conta}')
    elif operador == '-':
        conta = primeiro_numero_float - segundo_numero_float
        print(f'RESULTADO : {conta}')    
    elif operador == '/':
        conta = primeiro_numero_float / segundo_numero_float
        print(f'RESULTADO : {conta}')    
    elif operador == '*':
        conta = primeiro_numero_float * segundo_numero_float
        print(f'RESULTADO : {conta}')  
            
    sair = input('Quer sair? [s]im:').lower().startswith('s')
    if sair is True:
        break
          