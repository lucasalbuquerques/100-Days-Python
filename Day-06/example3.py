def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_move():
    turn_left()
    move()
    turn_right()


      
while not at_goal():
    if front_is_clear():
        move()
    else:
        while wall_in_front():
            jump_move()
        move()
        turn_right()
        while front_is_clear():
            move()
        turn_left()
        
        
    
    