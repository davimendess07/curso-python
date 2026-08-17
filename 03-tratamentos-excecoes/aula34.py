#66. while e break - Estrutura de repetição (Parte 1)

'''
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

Loop infinito --> Quando um código não tem fim

um circulo até alguma coisa acontecer
'''
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}') 

    if nome == 'sair':
        break

print('acabou')