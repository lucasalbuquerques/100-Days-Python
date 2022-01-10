# examples function with https://reeborg.ca/index_en.html
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_move():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    while not front_is_clear():
        jump_move()
    if not at_goal():
        move()
        
while not at_goal():
    if wall_in_front():
        jump_move
    else:
        move()
    
