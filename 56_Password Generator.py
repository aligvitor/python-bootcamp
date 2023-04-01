import random

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!#$%&()*+'

print("Bem-vindo ao gerador de senhas!")
nr_letras = int(input("Quantas letras você quer que sua senha tenha?\n")) 
nr_simbolos = int(input("Quantos simbolos você quer que sua senha tenha?\n"))
nr_numeros = int(input("Quantos números você quer que sua senha tenha?\n"))

senha = ''
for n in range(nr_letras):
    senha += random.choice(letras)

#não precisa de len, pq eu já coloco o número no input, logo o += vai fazer com que ele vai somando caracteres aleatórios até atingir o número do input

for n in range(nr_simbolos):
    senha += random.choice(simbolos)

for n in range(nr_numeros):
    senha += random.choice(numeros)

senha_lista = list(senha)
random.shuffle(senha_lista)

#join usado para cocatenar
senha_final = ''.join(senha_lista)

print("Sua senha é:", senha_final)