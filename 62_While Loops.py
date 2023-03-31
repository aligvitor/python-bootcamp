#while something_is_true
    #do something repeateadly


def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

numero_obstaculos = 6
while numero_obstaculos>0:
    jump()
    numero_obstaculos -=1
    print(numero_obstaculos)

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

