#44. Operadores in e not in

'''
Operadores in e not in
*Strings são interáveis
  0 1 2 3 4 5
  O t á v i o
 -6-5-4-3-2-1

 
 in: entre  (em portugues estar entre)
 not in: não entre  (em portugues estar não entre)

 interáveis - navegas item por item, utlizando os índices
 Eles verificam se um valor está dentro de alguma coleção
'''
nome = 'Otávio'
#print(nome[2])
#print(nome[-4])
'''
print('ávio' in nome)
print('zero' in nome)
print(10 * '-')
print('ávio' not in nome)
print('zero' not in nome)
'''
 #Eles verificam se um valor está dentro de alguma coleção
nome = input('digite seu nome: ') 
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')    