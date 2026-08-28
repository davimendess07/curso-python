'''
Interando strings com while
 
        0123456789
nome = 'Davi Ramos' #Iteráveis
        9876543210
  acessar o índice (exemlpo D) = print(nome[-10])

len = pegar o tamanho dos nomes
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

print(nome[3])
# tenho informação para fazer uma condição, 
# fazer um while, para inteirar sobre essa string,
#  para passar em cada uma dessas letras dentro do while 
#a cada inteiraçao do while, colocar um **, antes e dps da letra

letra = 0                    # 1. ponto de partida do contador
while tamanho_nome > letra:  # 2. condição — até quando rodar
letra += 1               # 3. avanço — atualiza o contador a cada volta
'''
'''
nome = input('qual seu nome? ')  # pega o valor do usuário
tamanho_nome = len(nome) # descobre quantas letras tem
letra = 0  # começa no índice 0
#o maior sempre vai ser o numero que n muda
while tamanho_nome > letra:  # continua enquanto ainda há letras
    print('*' + nome [letra]+ '*') 
    letra += 1 #avanço

''' 

nome = input('qual seu nome? ')  
tamanho_nome = len(nome) 
letra = 0  
nome_novo = ''

while tamanho_nome > letra:  
    letra_nova = nome[letra]
    nome_novo += f'*{letra_nova}'
    letra += 1 #avanço

nome_novo += '*'
print(nome_novo)    