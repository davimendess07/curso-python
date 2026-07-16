'''
37. O Debugger do VS Code e o interpretador do Python lendo códigos

-------------------------------ANOTAÇÕES----------------------------------------------
Entender o codigo com o Debuger to VScode
DeBug  = Depuração de código
Bug = inseto, problema no software
De = Tirar

Precisa informar o interpretador o Debuger (breackpoint)
'''
#if / elif         /else
#se / se não se / se não


condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:                                       #se essa condição for verdadeira
    print('Código para condição 1')                 #aparece isso

elif  condicao2:                                    #se não se
    print('Código para condição 2')                 #aparece isso

elif  condicao3:                                    #se não se
    print('Código para condição 3')                 #aparece isso

elif  condicao4:                                    #se não se
    print('Código para condição 4')                 #aparece isso

else:                                               #se não (nenhuma verdadeira)      
    print('Nenhuma condição satisfeita.')           #aparece isso

if 10 == 10:
    print('Outro if')
     
print('fora do if')   