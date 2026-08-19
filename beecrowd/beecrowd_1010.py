
cod_peca1, numero_peca1, valor_uni_peca1 = input().split()
cod_peca2, numero_peca2, valor_uni_peca2 = input().split()

cod_peca1 = int(cod_peca1)
numero_peca1 = float(numero_peca1)
valor_uni_peca1 = float(valor_uni_peca1)
cod_peca2 = int(cod_peca2)
numero_peca2 = float(numero_peca2)
valor_uni_peca2 = float(valor_uni_peca2)

total = (numero_peca1 * valor_uni_peca1) + (numero_peca2 * valor_uni_peca2)

print(f'VALOR A PAGAR: R$ {total:.2f}')

'''
cod_peca1 = int(input())
numero_peca1 = int(input())
valor_uni_peca1 = float(input())
cod_peca2 = int(input())
numero_peca2 = int(input())
valor_uni_peca2 = float(input())

#valor_peca1 = numero_peca1 * valor_uni_peca1
#valor_peca2 = numero_peca2 * valor_uni_peca2

total = (numero_peca1 * valor_uni_peca1) + (numero_peca2 * valor_uni_peca2)
# total = valor_peca1 + valor_peca2

print(f'VALOR A PAGAR: R$ {total:.2f}')
erro, aprendi ( input().split() )

Resumindo o que você aprendeu nesse problema (vale anotar):

input().split() quebra uma linha em pedaços por espaço, 
devolvendo texto (não número)
Atribuição múltipla (a, b, c = ...) exige que a quantidade 
de variáveis bata exatamente com a quantidade de pedaços

Pra converter depois, o padrão é variavel = tipo(variavel)
 — sobrescrevendo a mesma variável
Isso é uma introdução informal a listas (o que .split() devolve) 

— quando seu curso chegar nesse tópico formalmente, vai fazer ainda mais sentido o que rolou aqui
'''