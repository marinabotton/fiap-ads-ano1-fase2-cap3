# Solicita a quantidade de votos de cada dia da semana
segunda = int(input("> > > Digite a quantidade de votos para Segunda-Feira: "))
terca = int(input("> > > Digite a quantidade de votos para Terça-Feira: "))
quarta = int(input("> > > Digite a quantidade de votos para Quarta-Feira: "))
quinta = int(input("> > > Digite a quantidade de votos para Quinta-Feira: "))
sexta = int(input("> > > Digite a quantidade de votos para Sexta-Feira: "))

# Compara os votos e exibe o dia mais votado
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - - - - O dia escolhido foi SEGUNDA-FEIRA!  - - - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - - - - O dia escolhido foi TERÇA-FEIRA!  - - - - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - - - - O dia escolhido foi QUARTA-FEIRA! - - - - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - - - - O dia escolhido foi QUINTA-FEIRA! - - - - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
else:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - - - - O dia escolhido foi SEXTA-FEIRA!  - - - - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
