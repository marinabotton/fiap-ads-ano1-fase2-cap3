# Variável criada
bonus = ""

# Entrada de dados para saber qual o nível da assinatura do cliente
assinatura = input("> > > Digite o nível da assinatura: [1]Basic, [2]Silver, [3]Gold ou [4]Platinum ")

# Verifica a validade da assinatura
# Se inválida, apresenta mensagem de erro
if (assinatura != "1") and (assinatura != "2") and (assinatura != "3") and (assinatura != "4"):
    print("> > > Assinatura Inválida < < <")

# Se válida, pede a entrada de dados do faturamento anual do cliente
else:
    faturamento = float(input("> > > Digite o faturamento anual do cliente: "))

    # Calcula o bônus com base na assinatura
    if assinatura == "1":
        bonus = faturamento * 0.3
    elif assinatura == "2":
        bonus = faturamento * 0.2
    elif assinatura == "3":
        bonus = faturamento * 0.1
    elif assinatura == "4":
        bonus = faturamento * 0.05

    # Mostra o valor do bônus com duas casas decimais
    print("\n> > > O valor do bônus que o cliente deve pagar é: R$ {:.2f} < < <".format(bonus))
