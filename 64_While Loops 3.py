#while something_is_true
    #do something repeateadly

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
while at_goal() == False:
    if front_is_clear and right_is_clear():
        turn_right()
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    elif wall_on_right():
        move()
    if at_goal():
        done()

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

