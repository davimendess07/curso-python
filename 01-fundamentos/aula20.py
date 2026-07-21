'''
40. Solução - Exercício de programação com if e comparação

se um numero é maior ele aparece primeiro
se um numero é menor ele aparece segundo

*tabela unicold
como usar a f-string
'''
primeiro_numero = input('Entre com um numero: ')
segundo_numero = input('Entre com um numero: ')

if primeiro_numero > segundo_numero:
   # print(f'{primeiro_numero=}  é maior que o '{segundo_numero=}) 
    print(f"{primeiro_numero=} é maior que o {segundo_numero=}")
#usei f-string
elif primeiro_numero < segundo_numero:
   # print(f"{segundo_numero=}  é maior que o "{primeiro_numero=}) 
    print(f"{segundo_numero=} é maior que o {primeiro_numero=}")
#usei f-string

