#51. Interpolação de string com % em Python

'''
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

basicamente a mesma coisa que a gente fez com format, so que 
agora de um jeito diferente.

Só vc criar a string, colocar sinal de porcentagem na frente da string
e passar os valores para frente

'''

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco) #formataçao com interpolação
print(variavel)
print(10 * '-')
print('O hexadecimal de %d é %08X' % (1500, 1500))


#f-strings, format e interporlação

