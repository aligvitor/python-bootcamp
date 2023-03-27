#bill roulette
import random
# Import the random module here

# Split string method
names_string = input("Insira o nome de todos, separados por uma vírgula. ")
names = names_string.split(", ")

pessoa_que_vai_pagar = random.choice(names)

print(pessoa_que_vai_pagar + " vai pagar a conta hoje!")