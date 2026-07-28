#47. Fatiamento de strings e a função len


'''
Fatiamento de strings
012345678   índice começa do 0
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]

Obs.: a função len retona a qtd
de caracateres da str
'''
variavel = 'Olá Mundo'
print (len(variavel))
print (variavel[0:6])
print (variavel[0:9:4])
print (variavel[-1:-10:-1])  #inverte, vai por trás 
#-1 para inverter a leitura