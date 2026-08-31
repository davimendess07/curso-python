

''' 
km → milhas
kg → libras
celsius → fahrenheit
metros → pés

'''
calculadora_conversao = True
while calculadora_conversao:

    print('km para milhas = 1')
    print('kg para libras = 2')
    print('celsius para fahrenheit = 3')
    print('metros para pés = 4')
    conversao = input('Qual tipo de medida: ')

    validos = None #flag
    try: 
        conversao_float = int(conversao)
        validos = True

    except:
        validos =  None

    if validos is None:  
        print("Um dos valores são invalidos")
        continue

    conversao_permitidas = ['1','2','3','4']

    if conversao not in conversao_permitidas:
        print('Escolhas as opções da tabela!!')  
        continue  

    print('realizando sua conta!')  
    if conversao_float == 1:
             valor_km = float(input('entre com o valor do km: '))  
             conta_1 = valor_km * 0.6214
             print(f'RESULTADO = {conta_1:.2}')
    elif conversao_float == 2:
             valor_kg = float(input('entre com o valor do kg: '))
             conta_2 = valor_kg * 2.2046 
             print(f'RESULTADO = {conta_2:.2}')                 
    elif conversao_float == 3:
             valor_C = float(input('entre com o valor do celsius: ')) 
             conta_3 = (valor_C * 1.8) + 32
             print(f'RESULTADO = {conta_3:.2}')                 
    elif conversao_float == 4:
             valor_m = float(input('entre com o valor do metro: '))
             conta_4 = valor_m * 3.2808
             print(f'RESULTADO = {conta_4:.2}')     

    sair = input('Quer sair? [s]im:').lower().startswith('s')
    if sair is True:
            break                 
  
