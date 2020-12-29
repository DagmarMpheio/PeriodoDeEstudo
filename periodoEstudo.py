estudantes = int(input("Digite o numero de estudantes: "))
table={}
idade=0
cN=0
cM=0
estN={}
estM={}
for i in range(estudantes):
    nome = input("Digite o nome do estudante {0} :".format(i+1))
    anoNascimento = int(input("Digite o ano de nascimento do estudante {0} : ".format(i+1)))
    idade=2020 - anoNascimento
    if idade<19:
        print("A idade do(a) {0} eh {1}".format(nome, idade)," por isso sera tranferido para o periodo da manha\n")
        estM[nome]=idade
        cM=cM+1
    else:
        print("A idade do(a) {0} eh {1}".format(nome, idade), " por isso vai continuar no periodo noturno\n")
        estN[nome]=idade
        cN=cN+1
    table[nome] = idade
print(table)
print("{0} estudantes de manha: {1} e {2} estudante a noite: {3}".format(cM,estM.keys(),cN,estN.keys()))
