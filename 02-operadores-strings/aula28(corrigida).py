#49. Exercício: teste seu conhecimento até aqui (resolução)

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

'''  
                  O meu 
nome = input('Entre com seu nome: ')
idade = input('Entre com sua idade: ')
nome_invertido = nome[::-1]
if nome and idade:
    print(f"seu nome é: {nome}") #Seu nome é {nome}
    print(f"Seu nome invertido é: {nome_invertido}")
    print(' ' in nome) #Seu nome contém (ou não) espaços
    print(f"Seu nome tem {len(nome)} letras") #Seu nome tem {n} letras 
    print(f"A primeira letra do seu nome é: {nome[0]}")#A primeira letra do seu nome é {letra}
    print(f"A última letra do seu nome é {nome[-1]}")        
else:
    print("Desculpe, você deixou campos vazios.")     
    
    '''

nome = input('Entre com seu nome: ')
idade = input('Entre com sua idade: ')
nome_invertido = nome[::-1]
if nome and idade:
    print(f"seu nome é: {nome}") #Seu nome é {nome}
    print(f"Seu nome invertido é: {nome_invertido}")

#criei um if dentro de outro if (ai sim usei o "' ' in nome")
    if ' ' in nome:
        print('Seu nome contém espaços') #Seu nome contém (ou não) espaços
    else: 
        print('Seu nome não contém espaços') #Seu nome contém (ou não) espaços

    print(f"Seu nome tem {len(nome)} letras") #Seu nome tem {n} letras 
    print(f"A primeira letra do seu nome é: {nome[0]}")#A primeira letra do seu nome é {letra}
    print(f"A última letra do seu nome é {nome[-1]}") #A última letra do seu nome é {letra}       
else:
    print("Desculpe, você deixou campos vazios.") 

  