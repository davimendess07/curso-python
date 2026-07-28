#46. Formatação de strings com f-strings

'''
Formataçao básica de strings

s - string
d - int
f - float
.<número de dígito>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro 
= - Força o numero a aparecer antes dos zeros
Sinal - + ou -
Ex.:0>-100,.1f
Conversion flags - !r !s !a  ____repr____ ____str____ ____asc

#ped (largura fixa, so se ela n atingir 
a quantidade certa de caracter )
'''

variavel = 'ABC'          
print (f'{variavel}')
print (f'{variavel: >10}')
print (f'{variavel: <10}')
print (f'{variavel: ^10}')  
print (f'{1000.324342423423234:0=+10,.1f}') 
print (f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')
#f-strings