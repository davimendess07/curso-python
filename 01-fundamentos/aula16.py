'''
35. Introdução aos blocos de código + if / elif / els e (condicionais)

Operações condicionais
Bollean
Operadores
Blocos de códigos em pyhton

-------------------------------ANOTAÇÕES--------------------------------------------------
dps do "if" tenho que passar uma condição(pergunta eu tenho em retorno um dado Boolean (true) or (false))
dar tab para criar o bloco(4 espaços)

Condicionais são as estruturas que permitem ao programa tomar decisões com base em uma condição.

if /elif /else, dependem um do outro
unico que pode ser sozinho é o if, se tiver uma condição 
 '''

#if / elif         /else
#se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':               #a condição tem que ser verdadeira para ir para frente
    print('Você entrou no sistema')   #esse parte do código esta dentro do 'if'     
elif entrada == 'sair':               #elif é: se não for a primeira opção é a opção do bloco elif
    print('Você saiu do sistema')
else:                                 #sempre a ultima opção, se ele na digitou isso, faça isso. Sempre ter uma condição primeiro
    print('Você não digitou nem entrar nem sair.')    


#elif - pode se repetir varias vezes
