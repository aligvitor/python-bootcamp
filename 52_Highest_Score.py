# 🚨 Don't change the code below 👇
notas_alunos = input("Insira as notas dos alunos ").split()
for n in range(len(notas_alunos)):
  notas_alunos[n] = int(notas_alunos[n])

nota_maxima=(max(notas_alunos))
print("A nota máxima é ",nota_maxima)