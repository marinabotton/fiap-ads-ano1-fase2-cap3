assinaturas_validas = ["1", "2", "3", "4"]
assinatura = input("Digite o nível da assinatura ((1)Basic, (2)Silver, (3)Gold ou (4)Platinum): ")

if assinatura not in assinaturas_validas:
    print("Assinatura inválida")

else:
    faturamento = float(input("Digite o faturamento anual do cliente: "))

    if assinatura == "1":
        bonus = faturamento * 0.3
    elif assinatura == "2":
        bonus = faturamento * 0.2
    elif assinatura == "3":
        bonus = faturamento * 0.1
    elif assinatura == "4":
        bonus = faturamento * 0.05

    print("O valor do bônus que o cliente deve pagar é: R$ {:.2f}".format(bonus))
