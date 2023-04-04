assinatura = input("Digite o tipo de assinatura (Basic, Silver, Gold ou Platinum): ")

faturamento_anual = float(input("Digite o faturamento anual do cliente: "))

if assinatura == "Basic":
    porcentagem = 0.3
elif assinatura == "Silver":
    porcentagem = 0.2
elif assinatura == "Gold":
    porcentagem = 0.1
elif assinatura == "Platinum":
    porcentagem = 0.05
else:
    print("Assinatura inválida.")
    exit()

bonus = faturamento_anual * porcentagem

print("O valor do bônus que o cliente deve pagar é: R$ {:.2f}".format(bonus))
