#42. Operador Lógico "or"

'''
qualquer condiçao que for avaliada como verdadeira
avalai a condição inteira como verdadeira,
naquela condição verdadeira

Operadores Lógicos
and (e) or (ou) not (não)
and - Todas as condições precisam ser
verdadeiras
Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor
São considerados falsy (que vc já viu)
0, 0.0, '' , False
Também existe o tipo None que é
usado para representar um não valor


*and é usada para checar mais de uma expresão
*sempre que tiver uma expresao que tenha OR e AND na mesma expressão,
ela pode ficar ambigua

and:um false ele sai false
or: um or tudo vira true
'''

'''

               usando o or
entrada = input('[E]ntrar  [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
# if True:
#   ....
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')

else: 
    print('Sair')       
'''

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)

