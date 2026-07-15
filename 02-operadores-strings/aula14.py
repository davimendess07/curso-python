a = 'A'
b = 'B'
c = 1.1
string = 'a={nome1} a={nome1} b={nome2} c={nome3:.2f}'   
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )  #argumentos dentros, parametro #parametro nomeado

print(formato)


'''
tudo em python é um objeto
um objeto pode fazer açoes = metodos
metodos
índices, tudo que tem uma ordem começa no 0
"out of rang" = buscando algo que ja acabou/finalizou

quando a funçao (format) esta dentro de uma objeto(string) essa função 
é chamada de metodo

função format ou o fzin(f-strings)
nome3=parâmetro
a ou b ou c = argumento



nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))
'''
