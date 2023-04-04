# Inicializa as variáveis
soma_impar = 0
soma_par = 0
prox_impar = 0
prox_par = 0

# Solicita as notas dos alunos ímpares
print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS >>> ÍMPARES <<<:")
for x in range(1, 50, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    soma_impar += nota
    prox_impar += 1

# Solicita as notas dos alunos pares
print("AGORA, VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS >>> PARES <<<:")
for x in range(2, 51, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    soma_par += nota
    prox_par += 1

# Calcula as médias de cada grupo
media_impar = soma_impar / prox_impar
media_par = soma_par / prox_par

# Exibe a média dos grupos
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("- - - - - -  A MÉDIA DOS ALUNOS ÍMPARES FOI: {:.2f}!  - - - - - - -".format(media_impar))
print("- - - - - -   A MÉDIA DOS ALUNOS PARES FOI: {:.2f}!   - - - - - - -".format(media_par))
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

# Verifica qual grupo teve a maior média e imprime o resultado
if media_impar > media_par:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - O GRUPO DOS ALUNOS - ÍMPARES - OBTEVE A MAIOR MÉDIA!  - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
elif media_par > media_impar:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - -  O GRUPO DOS ALUNOS - PARES - OBTEVE A MAIOR MÉDIA!   - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
else:
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("- - - - - - OS DOIS GRUPOS OBTIVERAM A MESMA MÉDIA! - - - - - - -")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
