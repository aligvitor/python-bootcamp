import random
lista_palavras = ["Computador", "Escola", "Registro"]
lista_escolhida = random.choice(lista_palavras)
tamanho_da_palavra = len(lista_escolhida)

display = []

for letter in lista_escolhida:
        display += "_"

fim_do_jogo = False

while not fim_do_jogo: 
        guess = input("Advinhe uma letra e eu te digo se tem essa letra na palavra aleatória:\n")

        for position in range(tamanho_da_palavra):
                letter = lista_escolhida[position]
                if letter == guess:
                        display[position] = letter
                        
        print(display)
        
        if "_" not in display:
                end_of_game = True
                print("You won!")