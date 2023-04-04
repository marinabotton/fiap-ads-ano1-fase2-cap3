# Inicializa a variável
fatorial = 1

# Recebe os minutos atuais do usuário
minutos = int(input("Digite os minutos atuais da máquina: "))

# Validar dados de entrada
while minutos < 0 or minutos > 59:
    minutos = int(input("> > > Número inválido! Informe os minutos atuais da máquina: "))

# Calcula o fatorial dos minutos
for x in range(1, minutos + 1):
    fatorial *= x

# Exibe a senha de desbloqueio
print("A senha de desbloqueio é: LIBERDADE{}".format(fatorial))
