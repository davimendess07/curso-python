
'''
28. Concatenação (+) e repetição (*) com operadores aritméticos

Nesta aula, exploramos a concatenação e repetição de strings utilizando 
operadores aritméticos no Python. O operador de concatenação, representado pelo símbolo +,
permite unir duas ou mais strings. Por exemplo, se temos duas strings como "Olá" e "Mundo", 
a operação "Olá" + " " + "Mundo" resultará em "Olá Mundo".

A repetição é realizada com o operador *, que permite repetir uma string um número específico de vezes, 
desde que acompanhe um número inteiro. Por exemplo, ao realizar 'A' * 10, o resultado será 'AAAAAAAAAA',
repetindo a letra 'A' dez vezes. Isso é útil para criar padrões ou formatos de saída de texto de forma rápida e eficiente.

Ambos os operadores (concatenação e repetição) são essenciais para manipulação de strings em Python, 
oferecendo flexibilidade na forma como textualmente as informações são apresentadas. Ficou claro que a 
concatenação requer sempre o uso de strings, enquanto a repetição combina uma string com um inteiro para 
produzir a nova sequência desejada.
'''
concatenacao = 'A' + 'B' + 'C'
print(concatenacao)


concatenacao = 'Davi' + ' ' + 'Ramos' + ' ' + 'Mendes' + str(1)
print(concatenacao)

#quer colocar alguma numero? usa o coerção str(1)
#tomar cuidado com a tipagem


a_dez_vezes = 'A' * 10
tres_vezes_davi = 3 * 'Davi '
print(a_dez_vezes)
print(tres_vezes_davi, ' ')