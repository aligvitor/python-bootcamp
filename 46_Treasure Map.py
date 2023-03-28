row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

#map is a nested list
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
local_do_tesouro = input("Where do you want to put the treasure? ")

#aqui eu defino o que é a posição 0 do string (primeiro caractere) e a posição 1 (segundo caractere)
#não esquecer de converter para integer

horizontal = int(local_do_tesouro[0]) #primeiro número
vertical = int(local_do_tesouro[1]) #segundo número


#posso trocar que não dá nada
map[horizontal - 1][vertical - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")