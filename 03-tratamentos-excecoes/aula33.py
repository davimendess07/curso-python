#59. Conversa - tipos built-in, documentação, tipo imutávels, métodos de string

'''
"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
# outra_variavel = f'{string[:3]}ABC{string[4:]}'
# print(string)
# print(outra_variavel)
print(string.zfill(10))
'''

string = 'Davi Ramos'
outra_variavel = string
print(string.zfill(100))