'''
32. Precedência entre os operadores aritméticos

 Na aula 32, discutimos a precedência entre os operadores aritméticos em Python.
Esse conceito é fundamental para garantir que as expressões matemáticas sejam executadas corretamente.
O instrutor explica que a ordem de prioridade das operações é a seguinte: 
          primeiro, parênteses; 
          depois, potenciação;
          em seguida, multiplicação e divisão; 
          e, por último, adição e subtração.

 Um exemplo prático é apresentado, onde uma expressão que deveria resultar em 1024 retorna na verdade 7,
devido à ordem em que as operações são realizadas. Para corrigir isso, o uso de parênteses é sugerido para
forçar certas operações a serem executadas antes de outras. Além disso, o instrutor também fala sobre a possibilidade
de alterar o valor de uma variável durante a execução do programa, mostrando como isso pode afetar o resultado final.


'''

#1. (n+n) de dentro para fora
#2. **  potenciaçao
#3. * / // % (divisão, divisão_inteira e modulo) 
#4. + -     #executadas da esquerda para direita

conta_1 = 1+1 ** 5 + 5   #7        
print(conta_1)


conta_1 = (1+1) ** (5 + 5)    #1024   
print(conta_1)





'''
Sobre o int(0.5 + 0.5): o int é uma função em Python que converte um valor em um número inteiro. Neste caso, 0.5 + 0.5 resulta
em 1.0, e ao passar isso para a função int, o resultado final é 1. Isso acontece porque a função int remove a parte decimal e 
retorna só a parte inteira.
'''
conta_1 = (1+ int(0.5 +0.5)) ** (5 + 5)    #1024   #trocamos o "1" por dois "0.5" e adicionamos mais um par de parênteses  
print(conta_1)



'''
                      Trocar o valor de uma variável em Python 
é bastante simples. Você pode simplesmente atribuir um novo valor à variável usando o operador de atribuição (=). Por exemplo:
  x = 10  # Inicialmente, x tem o valor 10
  x = 20  # Agora, x tem o valor 20


  Quando você faz isso, o interpretador Python lê a linha de código de cima para baixo e da esquerda para a direita. Portanto,
   a variável x inicialmente contém 10, e a segunda atribuição troca esse valor para 20.

Um ponto importante a ser lembrado é que, embora você possa trocar o valor de uma variável a qualquer momento no seu código, 
essa prática pode dificultar a compreensão do que o programa está fazendo, especialmente em códigos maiores. É recomendado criar 
novas variáveis em vez de sobrescrever valores, para manter seu código mais claro e evitar confusões.
'''