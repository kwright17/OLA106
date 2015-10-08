def turn_right():
    turn_left()
    turn_left()
    turn_left()   
##face North 
def face_north():
    
        while not facing_north():
            turn_left()
##find vestibule
def go_outside():
    while not left_is_clear():
        
        if right_is_clear():
            if not front_is_clear():
                turn_right()
            move()
        else:
            move()
    
        
def exit_vest():
    if not right_is_clear():
        move()
    else:
        turn_left()
        move()
    if not left_is_clear():
        move()
        turn_left()
        move()
        
        
    
