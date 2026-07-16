'''
38. Usando a função input para coletar dados do usuario

coersao de strings
como pegar o nome da variavel e o valor da variavel (ex: nome='João)
---------------------------------------------------------------------------------

numero_1 = input('Digite um número: '))   
numero_2 = input('Digite outro número: '))
print(f'A soma dos números é: {numero_1 + numero_2}')   #acontece a concatenação

---------------------------------------------------------------------------------
nome = input('Qual o seu nome? ') sempre vai receber str
print(f'O seu nome é {nome}')
---------------------------------------------------------------------------------
numero_1 = int(input('Digite um número: '))  #fazer o type casting (coerção de tipo)  
numero_2 = int(input('Digite outro número: '))

print(f'A soma dos números é: {numero_1 + numero_2}') 
agora funcionou por conta que fiz a coerção de tipo (de str para int)... antes estava concatenando os valores que eu colocava no input

---------------------------------------------------------------------------------
'''
numero_1 = input('Digite um número: ')  
numero_2 = input('Digite outro número: ')

#aqui fariamos uma checagem de numeros  

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')   