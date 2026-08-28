#69. while + continue - pulando alguma repetição

'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

Loop infinito --> Quando um código não tem fim

um circulo até alguma coisa acontecer
'''
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('nao vou mostar o 6. ')
        continue 

    if contador >= 10 and contador <= 27:
        print('nao vou mostar o', contador)
        continue  #fez uma condição para pular certos numeros (usando o continue)


    print(contador)  

    if contador == 40:
        break      #quebra o laço de acordo com a condição

print('Acabou')    