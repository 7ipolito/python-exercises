dictAluno = {}
nome = input("Digite o nome do aluno")
dictAluno["nome"] = nome
media = int(input("Digite a media do aluno"))
dictAluno["media"] = media
situacao = ""
if media > 7:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"
dictAluno["situacao"] = situacao

alunos =[]
alunos.append(dictAluno)
for i, aluno in enumerate(alunos, start=1):
    print(f"\nAluno {i}:")
    print(f"  Nome: {aluno['nome']}")
    print(f"  Média: {aluno['media']}")
    print(f"  Situação: {aluno['situacao']}")