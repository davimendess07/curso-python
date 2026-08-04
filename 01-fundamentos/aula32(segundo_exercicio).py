
print ('Faça um programa que pergunte a hora ao usuário e,\
baseando-se no horário descrito, exiba a saudação apropriada.\
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.')
print('')
print('')
print('')

horario = input('me fale o horario: ')
horario_correto = int(horario)
if horario_correto <= 11:
    print(f'Bom dia, são: {horario} da manhã')
elif horario_correto >=12 and horario_correto < 17:
    print(f'Boa Tarde, são: {horario} da tarde')
elif horario_correto > 18 and horario_correto < 23:
    print(f'Boa Noite, são: {horario} da noite')    

