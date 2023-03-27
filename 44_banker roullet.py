#bill roulette
import random
# Import the random module here

# Split string method
names_string = input("Insira o nome de todos, separados por uma vírgula. ")
names = names_string.split(", ")

num_itens = len(names)

random_choice = random.randint(0, num_itens - 1)
pessoa_que_vai_pagar = names[random_choice]

print(pessoa_que_vai_pagar + " vai pagar a conta hoje!")