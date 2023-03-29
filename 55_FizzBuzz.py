total=0
for numero in range(1, 101):
        if numero % 3 ==0 and numero % 5 ==0:
                print("FizzBuzz")
#elif é a abreviação para else if -> se a condição de if não for atendida, o algoritmo vai para os elifs
        elif numero % 3 ==0:
                print("Fizz")
        elif numero % 5 ==0:
                print("Buzz")
        else:
                total = numero                                                                
        print(total)