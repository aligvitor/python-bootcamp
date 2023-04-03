import random
lista_palavras = ["Computador", "Escola", "Registro"]

lista_escolhida = random.choice(lista_palavras)

guess = input("Advinhe uma letra e eu te digo se tem essa letra na palavra aleatória:\n").lower()

display = []

for letter in lista_escolhida:
        display += "_"

tamanho_da_palavra = len(lista_escolhida)

for position in range(tamanho_da_palavra):
        letter = lista_escolhida[position]
        if letter == guess:
                display[position] = letter
                
print(display)