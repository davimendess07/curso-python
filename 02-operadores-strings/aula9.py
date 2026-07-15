#27. Introdução aos operadores aritméticos (matemática)
'''
Nesta aula, abordamos os operadores aritméticos em Python. 
Começamos com a adição, subtração, multiplicação e divisão, 
explicando que a adição utiliza o sinal de mais, enquanto a 
subtração usa o sinal de menos. A multiplicação é feita com o 
asterisco, e a divisão normal sempre retorna um número em ponto 
flutuante.

Destacamos também a divisão inteira, que utiliza duas barras e 
retorna apenas a parte inteira do resultado. A exponenciação,
 que eleva um número a outro, e o operador módulo, que retorna o resto da divisão, 
 também foram discutidos, sendo este último útil para verificar se um número é par ou ímpar.

Foram dados exemplos práticos, como a verificação de divisibilidade, 
e concluímos que os operadores aritméticos são fundamentais na programação em Python, 
com a promessa de explorar mais sobre eles nas próximas aulas.
'''


adicao = 10 + 10  #Não é possível usaro sinal de + com int e str
                  #apenas int/float e str/str.
print('Adição', adicao)

subtracao = 10 - 5 
print('Subtração', subtracao)

multiplicação = 5 * 5 
print('Multiplicação', multiplicação)

divisao = 10 / 5
print('Divisão', divisao)

divisao_inteira = 10 // 3 
print('Divisão Inteira', divisao_inteira)

exponenciaçao = 2 ** 10
print('Exponenciação', exponenciaçao)

modulo = 55 % 2  #resto da divisao
print('Modulo', modulo)

print(10 % 8 == 0) 
print(16 % 8 == 0) 
print(10 % 2 == 0)  #numero é par se ele é divisivel por 2!
print(16 % 2 == 0) 



