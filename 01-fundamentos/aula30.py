#57. Parte 1: Variáveis, constantes e complexidade de código

'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no memso if (ruim)
            <- Contagem de complexidade (ruim)
'''

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro esta na estrada


RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                       local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_mutlado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

# se ele passou da velocidade do radar
if vel_carro_pass_radar_1:
    print('Velocidade carro passou o radar 1')
#se ele so passou pelo radar
if carro_passou_radar_1:
    print('Carro passou radar 1')
#ver se o carro tomou multa ou não
if  carro_passou_radar_1 and vel_carro_pass_radar_1:  
    print('Carro multado em radar 1')





# else:
#     print('velocidade normal')    



'''
boas praticas de programação
como pensar para escrever programas para outras pessoas 

letras maiúsculas para variáveis constante
o codigo tem que ser facil de ler

variável não é para resumir o codigo, mas sim
deixar o codigo mais limpo
'''