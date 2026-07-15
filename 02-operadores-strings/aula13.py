'''
32. Uma introdução às f-strings (formatação de strings)

nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = ... 
'''


nome = 'Davi Ramos Mendes'
altura = 1.80
peso = 80
imc = peso / (altura * altura)  #ou peso /  altura ** 2
                                #usei exponenciação, divisão, parêntese, 

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'  #so de colocar o 'f', eu ja habilito usar variáveis dentro do print, devolvo ela em chaves
linha_2 = f'pesa {peso} quilos e seu IMC é'     #:.2f casas decimais
linha_3 = f'{imc:.2f}'                          #:,.2f casas decimais (para dinheiro)
                                                  
#print(nome, 'tem', altura, 'de altura,')
print(linha_1)
print(linha_2)
print(linha_3)

# tupla
#IMC = peso / (altura x altura) ou peso / (altura **)



'''
strings, uma forma prática de formatar strings em Python. 
Ele ressalta a importância de usar strings de forma eficiente 
e como isso pode facilitar a programação. O foco é mostrar que 
as f-strings permitem incluir variáveis diretamente dentro das 
strings, usando um 'f' antes das aspas e chaves para as variáveis.

O professor exemplifica isso com uma string que contém o nome e 
a altura de uma pessoa, demonstrando a renderização correta das 
variáveis. Também discute a formatação de números, como a definição 
de casas decimais, especialmente útil para valores monetários. 
Há uma breve demonstração de como formatar um número em reais. 
Ele destaca que a formatação de strings é uma habilidade essencial 
e que as f-strings são uma introdução eficaz, com mais tópicos sobre 
formatação a serem abordados em aulas futuras.

'''