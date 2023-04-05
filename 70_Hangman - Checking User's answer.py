import random
lista_palavras = ["Computador", "Escola", "Registro"]

lista_escolhida = random.choice(lista_palavras)

guess = input("Advinhe uma letra e eu te digo se tem essa letra na palavra aleatória:\n").lower()

for letter in lista_escolhida:
    if letter == guess:
        print("Acertô!")
    else:
        print("Errooou!")

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.