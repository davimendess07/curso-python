'''
36. if, elif e else: entendendo o fluxo do interpretador em condicionais

-------------------------------ANOTAÇÕES--------------------------------------------------
*Condição

o fluxo do if, vai checar tudo, vai executar so uma condição
se precisar cria outro if

(else) sempre o contrario de if

(if) so é executado se a condição for verdadeira

para eu colocar outra condição eu coloco o elif
'''
#if / elif         /else
#se / se não se / se não


condicao1 = True
condicao2 = True
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