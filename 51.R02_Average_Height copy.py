altura_estudantes = input("Insira a altura dos estudantes aqui (em centímetros): ").split()

# Converter cada altura para um número inteiro
for i in range(len(altura_estudantes)):
    altura_estudantes[i] = int(altura_estudantes[i])

# Calcular a soma das alturas
soma_alturas = 0
for altura in altura_estudantes:
    soma_alturas += altura


numero_estudantes = (len(altura_estudantes))

altura_media = round(soma_alturas/numero_estudantes)

print("A soma das alturas é:", soma_alturas, "para um total de", numero_estudantes, "de estudantes, tendo uma média total de", altura_media, "centimetros de altura")
