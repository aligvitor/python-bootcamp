import random
lista_palavras = ["Computador", "Escola", "Registro"]

lista_escolhida = random.choice(lista_palavras)

display = []

for letter in lista_escolhida:
        display += "_"
        
        
print(display)