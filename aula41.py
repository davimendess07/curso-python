#76. while / else (recurso peculiar do Python)

'''
while / else
'''

string = 'Valorqualquer'

i = 0 
while i < len(string):
    letra = string[i]


    if letra == ' ':
        break

    print(letra)
    i += 1

else:  #quando o laço do while executa completamente, o else aparece
    print('não a espaço na palavra')
print('fora do while')          

# break   caso isso acontecer, ele ja pula para fora do while
# como usar o else no while