soma_impar = 0
soma_par = 0
count_impar = 0
count_par = 0

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
for x in range(1, 50, 2):
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}: "))
    soma_impar += nota
    count_impar += 1

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
for x in range(2, 51, 2):
    nota = float(input(f"POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}: "))
    soma_par += nota
    count_par += 1

media_impar = soma_impar / count_impar
media_par = soma_par / count_par

if media_impar > media_par:
    print("O grupo dos alunos ímpares teve a maior nota.")
elif media_par > media_impar:
    print("O grupo dos alunos pares teve a maior nota.")
else:
    print("Os dois grupos tiveram a mesma nota.")
