rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

escolha_usuario = input("Escolha pedra, papel ou tesoura \n")

escolha_usuario.lower()

acoes_pc_possiveis = ["pedra", "papel", "tesoura"]
acoes_pc_real = random.choice(acoes_pc_possiveis)

if escolha_usuario == acoes_pc_real:
    print(f"Os dois selecionaram {escolha_usuario}. Deu empate!")
elif escolha_usuario == "pedra":
    if acoes_pc_real == "tesoura":
        print("Pedra amassa tesoura! Você venceu, caralho!")
    else:
        print("Papel cobre pedra! Sifodeu!.")
elif escolha_usuario == "papel":
    if acoes_pc_real == "pedra":
        print("Papel cobre pedra! Você venceu, caralho!")
    else:
        print("Tesoura corta papel! Sifodeu!")
elif escolha_usuario == "tesoura":
    if acoes_pc_real == "papel":
        print("Tesoura corta papel! Você venceu, caralho!")
    else:
        print("Pedra amassa tesoura! Sifodeu!")